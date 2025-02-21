from setuptools import setup, find_packages

setup(
    name="webpage2md",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pypandoc",
        "pytest-playwright",
        "beautifulsoup4",
        "httpx",
    ],
    entry_points={
        'console_scripts': [
            'webpage2md=webpage2md:main',
        ],
    },
)
