# MultiAgentX

A flexible framework for building multi-agent systems.

## Installation

### Install from source

You can install the package directly from source:

```bash
pip install .
```

For development installation:

```bash
pip install -e .
```


### Install from pypi

You can install the package from pypi

```bash
pip install multiagentx -i https://pypi.org/simple
```

You can also upgrade the package from pypi

```bash
pip install multiagentx --upgrade -i https://pypi.org/simple
```

## Usage


```python
from multiagentx import hello
hello()
```


## Package Upload

First time upload

```bash
pip install build twine
python -m build
twine upload dist/*
```

Subsequent uploads

```bash
rm -rf dist/ build/ *.egg-info/
python -m build
twine upload dist/*
```


