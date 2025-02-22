# neatoo
A simple yet powerful tool for Python code formatting, checking, and testing.

neatoo is built on top of [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort), and [flake8](https://github.com/PyCQA/flake8), thanks to those great tools.

## Installation

1. Install from pip:
```bash
pip install neatoo
```

2. Install from source:
```bash
pip install -e .
```

## Usage:

1. format your code:
```bash
neatoo format {paths}
```

2. check your code:
```bash
neatoo check {paths}
```

3. test your code:
This is equivalent to running `pytest` on the `tests/` directory.

```bash
neatoo test {paths}
```


