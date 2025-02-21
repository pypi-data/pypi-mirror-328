# MultiAgentX

A flexible framework for building multi-agent systems.

## Installation

You can install the package directly from source:

```bash
pip install .
```

For development installation:

```bash
pip install -e .
```


# upload to pypi

```bash
pip install build twine
python -m build
twine upload dist/*
```

# update code and upload to pypi

```bash
rm -rf dist/ build/ *.egg-info/
python -m build
twine upload dist/*
```

# Usage

```bash
pip install multiagentx
```

```python
from multiagentx import hello
hello()
```


