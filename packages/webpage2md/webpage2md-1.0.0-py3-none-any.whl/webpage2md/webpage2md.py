#!/usr/bin/env python

import re
import sys
import subprocess
import os
import argparse
from urllib.parse import urlparse
from pathlib import Path

import pypandoc

__version__ = "1.0.0"
user_agent = f"WEBPAGE2MD/{__version__}"

# Playwright is nice because it has a simple way to install dependencies on most
# platforms.


def install_playwright():
    """Install playwright and its dependencies if not already installed"""
    try:
        from playwright.sync_api import sync_playwright
        # First try to launch browser to check if everything is installed
        with sync_playwright() as p:
            p.chromium.launch()
        return True
    except ImportError:
        print("Installing playwright...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pytest-playwright"], check=True)
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing playwright: {e}")
            return False
    except Exception as e:
        print("Installing browser...")
        try:
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
            # Verify installation worked
            with sync_playwright() as p:
                p.chromium.launch()
            return True
        except Exception as e2:
            print(f"Error installing browser: {e2}")
            return False


class Scraper:
    pandoc_available = None
    playwright_available = None
    playwright_instructions_shown = False

    # Public API...
    def __init__(self, print_error=None, playwright_available=None, verify_ssl=True):
        """
        `print_error` - a function to call to print error/debug info.
        `verify_ssl` - if False, disable SSL certificate verification when scraping.
        """
        if print_error:
            self.print_error = print_error
        else:
            self.print_error = print

        self.playwright_available = playwright_available
        self.verify_ssl = verify_ssl

    def scrape(self, url):
        """
        Scrape a url and turn it into readable markdown if it's HTML.
        If it's plain text or non-HTML, return it as-is.

        `url` - the URL to scrape.
        """

        if self.playwright_available:
            content, mime_type = self.scrape_with_playwright(url)
        else:
            content, mime_type = self.scrape_with_httpx(url)

        if not content:
            self.print_error(f"Failed to retrieve content from {url}")
            return None

        # Check if the content is HTML based on MIME type or content
        if (mime_type and mime_type.startswith("text/html")) or (
            mime_type is None and self.looks_like_html(content)
        ):
            self.try_pandoc()
            content = self.html_to_markdown(content)

        return content

    def looks_like_html(self, content):
        """
        Check if the content looks like HTML.
        """
        if isinstance(content, str):
            # Check for common HTML tags
            html_patterns = [
                r"<!DOCTYPE\s+html",
                r"<html",
                r"<head",
                r"<body",
                r"<div",
                r"<p>",
                r"<a\s+href=",
            ]
            return any(re.search(pattern, content, re.IGNORECASE) for pattern in html_patterns)
        return False

    # Internals...
    def scrape_with_playwright(self, url):
        import playwright  # noqa: F401
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            try:
                browser = p.chromium.launch()
            except Exception as e:
                self.playwright_available = False
                self.print_error(str(e))
                return None, None

            try:
                context = browser.new_context(ignore_https_errors=not self.verify_ssl)
                page = context.new_page()

                user_agent = page.evaluate("navigator.userAgent")
                user_agent = user_agent.replace("Headless", "")
                user_agent = user_agent.replace("headless", "")
                user_agent += " " + user_agent

                page.set_extra_http_headers({"User-Agent": user_agent})

                response = None
                try:
                    response = page.goto(url, wait_until="networkidle", timeout=5000)
                except PlaywrightTimeoutError:
                    self.print_error(f"Timeout while loading {url}")
                except PlaywrightError as e:
                    self.print_error(f"Error navigating to {url}: {str(e)}")
                    return None, None

                try:
                    content = page.content()
                    mime_type = None
                    if response:
                        content_type = response.header_value("content-type")
                        if content_type:
                            mime_type = content_type.split(";")[0]
                except PlaywrightError as e:
                    self.print_error(f"Error retrieving page content: {str(e)}")
                    content = None
                    mime_type = None
            finally:
                browser.close()

        return content, mime_type

    def scrape_with_httpx(self, url):
        import httpx

        headers = {"User-Agent": f"Mozilla/5.0 ({user_agent})"}
        try:
            with httpx.Client(
                headers=headers, verify=self.verify_ssl, follow_redirects=True
            ) as client:
                response = client.get(url)
                response.raise_for_status()
                return response.text, response.headers.get("content-type", "").split(";")[0]
        except httpx.HTTPError as http_err:
            self.print_error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            self.print_error(f"An error occurred: {err}")
        return None, None

    def try_pandoc(self):
        if self.pandoc_available:
            return

        try:
            pypandoc.get_pandoc_version()
            self.pandoc_available = True
            return
        except OSError:
            pass

        try:
            pypandoc.download_pandoc(delete_installer=True)
        except Exception as err:
            self.print_error(f"Unable to install pandoc: {err}")
            return

        self.pandoc_available = True

    def html_to_markdown(self, page_source):
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(page_source, "html.parser")
        soup = slimdown_html(soup)
        page_source = str(soup)

        if not self.pandoc_available:
            return page_source

        try:
            md = pypandoc.convert_text(page_source, "markdown", format="html")
        except OSError:
            return page_source

        md = re.sub(r"</div>", "      ", md)
        md = re.sub(r"<div>", "     ", md)

        md = re.sub(r"\n\s*\n", "\n\n", md)

        return md


def slimdown_html(soup):
    for svg in soup.find_all("svg"):
        svg.decompose()

    if soup.img:
        soup.img.decompose()

    for tag in soup.find_all(href=lambda x: x and x.startswith("data:")):
        tag.decompose()

    for tag in soup.find_all(src=lambda x: x and x.startswith("data:")):
        tag.decompose()

    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr != "href":
                tag.attrs.pop(attr, None)

    return soup


def make_safe_filename(path):
    """Create a safe filename from a URL or file path"""
    if is_url(path):
        # Get the last part of the URL, removing query parameters
        filename = urlparse(path).path.split('/')[-1] or urlparse(path).netloc
    else:
        # Get just the filename from the path
        filename = os.path.basename(path)
    
    # Remove the extension if present
    filename = os.path.splitext(filename)[0]
    
    # Replace unsafe characters
    safe_filename = re.sub(r'[^a-zA-Z0-9-]', '_', filename)
    return f"{safe_filename}.md"

def is_url(string):
    """Check if the string is a URL"""
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def read_local_file(filepath):
    """Read content from a local HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read(), "text/html"
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None, None

def process_input(path, args, scraper):
    """Process a single input file or URL"""
    # Ensure playwright is installed if we're dealing with a URL
    if is_url(path) and not install_playwright():
        print("Failed to install/verify playwright. Please install manually:")
        print("pip install pytest-playwright")
        print("playwright install --with-deps chromium")
        sys.exit(1)
    
    if is_url(path):
        content = scraper.scrape(path)
    else:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return None
        content, _ = read_local_file(path)
        if content and scraper.looks_like_html(content):
            scraper.try_pandoc()  # Ensure pandoc is available
            content = scraper.html_to_markdown(content)
            
    return content

def main():
    parser = argparse.ArgumentParser(description='Convert HTML files or URLs to Markdown')
    parser.add_argument('inputs', nargs='+', help='One or more HTML files or URLs')
    parser.add_argument('-o', '--output-dir', help='Output directory for markdown files')
    parser.add_argument('-n', '--name', help='Output filename (only works with single input)')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output except for errors')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed processing information')
    parser.add_argument('--stdout', action='store_true', help='Print markdown to stdout instead of saving')
    
    args = parser.parse_args()
    
    # Create output directory if specified
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
    
    # Validate single output name with multiple inputs
    if args.name and len(args.inputs) > 1:
        print("Error: Cannot specify output name with multiple inputs")
        sys.exit(1)
    
    scraper = Scraper()
    
    for path in args.inputs:
        if args.verbose:
            print(f"Processing: {path}")
            
        content = process_input(path, args, scraper)
        
        if not content:
            if not args.quiet:
                print(f"Failed to process: {path}")
            continue
            
        if args.stdout:
            print(content)
            continue
            
        # Determine output filename
        if args.name and len(args.inputs) == 1:
            output_file = args.name if args.name.endswith('.md') else f"{args.name}.md"
        else:
            output_file = make_safe_filename(path)
            
        # Add output directory if specified
        if args.output_dir:
            output_file = os.path.join(args.output_dir, output_file)
            
        # Save the file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        if not args.quiet:
            print(f"Saved markdown to: {output_file}")
            if not args.stdout:
                print("\nContent preview:")
                print("----------------")
                print(content[:500] + "..." if len(content) > 500 else content)

if __name__ == "__main__":
    main()
