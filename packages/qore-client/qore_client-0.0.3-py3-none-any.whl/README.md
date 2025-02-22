# Qore Client

Qore Client is a Python client library for the Qore API.

## Installation

```bash
pip install qore-client
```

## Development Environment Setup

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create a virtual environment and install dependencies

```bash
uv venv

source .venv/bin/activate  # Linux/Mac
# or
.\.venv\Scripts\activate  # Windows
```

3. Install the base package

```bash
uv pip install -e .
```

4. Install the development dependencies

```bash
uv pip install -e ".[dev]"
```

## Deployment

The project can be deployed to TestPyPI and PyPI:

```bash
# Deploy to TestPyPI
./deploy.sh test

# Deploy to PyPI
./deploy.sh prod
```

## CI/CD

This project supports automated testing and deployment through GitLab CI/CD.

## Test

```bash
# Install the package from TestPyPI
uv pip install -i https://test.pypi.org/simple/ qore-client=={version}

# Install the package from PyPI
uv pip install qore-client=={version}
```
