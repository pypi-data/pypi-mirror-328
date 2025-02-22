# PKU - PKMN Utility Library

[![Codeberg repository](https://img.shields.io/badge/Repository-Codeberg-blue?logo=codeberg&labelColor=white&style=plastic)][repo]
[![CPython 3.12 to 3.14](https://img.shields.io/badge/CPython-3.12%20|%203.13%20|%203.14-blue?style=plastic)][python]
[![PyPI version](https://img.shields.io/pypi/v/pku-lib?label=PyPI&color=blue&style=plastic)][pypi]
[![AGPLv3+ license](https://img.shields.io/pypi/l/pku-lib?label=License&color=blue&style=plastic)][license]

<p align=center>
    <img src="https://codeberg.org/wry/pku-lib/raw/branch/main/assets/icon.png" title="Pyukumuku" alt="Pyukumuku sprite">
</p>

## Installation

This library supports [CPython][python] 3.12 to 3.14.

1. Install the package from [PyPI] **(recommended)**

- The latest stable release.
- Potentially outdated.

```shell
python3 -m pip install pku-lib
```

2. Install the package from [Codeberg][repo]

- The most recent changes.
- Potentially unstable.

```shell
python3 -m pip install git+https://codeberg.org/wry/pku-lib.git
```

## Usage

To use the library, import `pku`.

```python
import pku

pku.hello()
```

## Development

1. **Install uv**

[uv](https://docs.astral.sh/uv/) is a tool for managing dependencies and
running tests. See the uv documentation for installation instructions.

2. **Set Up the Development Environment**

Once uv is installed, run the following command to ensure that all project
dependencies are installed and up-to-date.

```shell
uv sync
```

3. **Lint and Run Tests**

To ensure your code is consistent with the project and passes current tests,
run nox:

```shell
uv run nox
```

## License

This library is licensed under the [GNU Affero General Public License][license]
version 3.0 or later.

<!-- Hyperlinks! -->

[python]: https://python.org/downloads/ "Download Python"
[pypi]: https://pypi.org/project/pku-lib/ "Python Package Index"
[repo]: https://codeberg.org/wry/pku-lib/ "Codeberg repository"
[license]: https://www.gnu.org/licenses/agpl-3.0.en.html "GNU Affero General Public License"
