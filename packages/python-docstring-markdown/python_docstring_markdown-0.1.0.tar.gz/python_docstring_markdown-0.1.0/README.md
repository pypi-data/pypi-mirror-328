# python-docstring-markdown

A Python module and CLI that walks a Python package/directory and outputs a Markdown file from all docstrings in the package.

## Features

- Crawls the packages, modules, classes, functions, and methods using the `ast` module
- Auto-detects ReST, Google, Numpydoc-style and Epydoc docstrings using [`docstring-parser-fork`](https://pypi.org/project/docstring-parser-fork/)
- Generates a table of contents with anchor links
- Tracks and documents module exports (`__all__`)
- Preserves module hierarchy in documentation
- Handles nested classes and functions

## Installation

```bash
pip install python-docstring-markdown
```

## Usage

### Command Line

```bash
python -m python_docstring_markdown <package_dir> <output_file>
```

Arguments:
- `package_dir`: Path to your Python package directory
- `output_file`: Path where the Markdown documentation file will be saved

Example:
```bash
python -m python_docstring_markdown ./src/my_package docs/api.md
```

### Python API

```python
from python_docstring_markdown import crawl

# Generate documentation for a package
docs_content = crawl("./src/my_package")

# Save to a file
with open("docs/api.md", "w") as f:
    f.write(docs_content)
```

## Contributing

I welcome feedback and contributions!

## License

CC-0 1.0 Universal. See the [LICENSE](LICENSE) file for more information.
