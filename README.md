[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

This project will be deprecated in the near future. All the functionality has been moved to the new [repository](https://github.com/multiversx/mx-sdk-py).

The migration guide as a GitHub issue can be found [here](https://github.com/multiversx/mx-sdk-py/issues/41).

# mx-sdk-py-core

Core components of the MultiversX Python SDK.

## Distribution
 
 - GitHub: `git+https://git@github.com/multiversx/mx-sdk-py-core.git@v{Version}#egg=multiversx_sdk_core`
 - [PyPi](https://pypi.org/user/multiversx/)

## Documentation

[docs.multiversx.com](https://docs.multiversx.com/sdk-and-tools/erdpy/erdpy/)

## Development setup

### Virtual environment

Create a virtual environment and install the dependencies:

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt --upgrade
```

Install development dependencies, as well:

```
pip install -r ./requirements-dev.txt --upgrade
```

Above, `requirements.txt` should mirror the **dependencies** section of `pyproject.toml`.

If using VSCode, restart it or follow these steps:
 - `Ctrl + Shift + P`
 - _Select Interpreter_
 - Choose `./venv/bin/python`.

### Tests

Run the tests as follows:

```
pytest .
```

### Linting

First, install [`pyright`](https://github.com/microsoft/pyright) as follows:

```
npm install --global pyright
```

Run `pyright`:

```
pyright
```

Run `flake8`:

```
flake8 multiversx_sdk_core
```
