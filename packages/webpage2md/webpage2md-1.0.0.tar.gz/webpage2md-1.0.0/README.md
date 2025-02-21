# webpage2md

A command-line tool to convert HTML files and web pages to Markdown format.

## Features

- Convert local HTML files to Markdown
- Convert web pages to Markdown
- Support for multiple input files
- Custom output directory and filename options
- Automatic installation of required dependencies
- Uses Playwright for reliable web scraping
- Uses Pandoc for high-quality HTML to Markdown conversion

## Installation

```bash
pip install webpage2md
```

## Usage

### As a Python Package

```python
from webpage2md import convert_html, convert_url

# Convert HTML string to markdown
html = '<h1>Hello World</h1>'
markdown = convert_html(html)

# Convert webpage to markdown
markdown = convert_url('https://example.com')
```

### Command Line Usage

Basic usage:
```bash
webpage2md example.html                  # Convert local file
webpage2md https://example.com          # Convert web page
webpage2md file1.html file2.html        # Convert multiple files
```

Options:
```bash
webpage2md -o output_dir/ file.html     # Specify output directory
webpage2md -n custom_name.md file.html  # Specify output filename
webpage2md --stdout file.html           # Print to stdout
webpage2md -q file.html                 # Quiet mode
webpage2md -v file.html                 # Verbose mode
```

For help:
```bash
webpage2md --help
```

## Requirements

- Python 3.7+
- Playwright (automatically installed)
- Pandoc (automatically installed)

## License

MIT License
