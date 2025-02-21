# importsearch

importsearch is a tool for scanning and auditing your Python scripts for all imported modules. It helps you quickly understand your project's dependencies by parsing your source files and listing every module that is imported.

## Features

- **Dependency Audit:** Provides a clear list of external libraries and modules your project relies on.

## installs
[![PyPI Downloads](https://static.pepy.tech/badge/importsearch)](https://pepy.tech/projects/importsearch)

## Installation

You can install importsearch using pip:

```bash
pip install importsearch
```

## Usage

### Function Form (preferred)

absolute path to the target file is preferred

```python
import importsearch

target_file = 'path/to/your/file.py'
importsearch.search(target_file)
```

### class Form
```python
import importsearch
target_file = 'path/to/your/file.py'
search = importsearch(target_file, debug=True)
search.search()
```