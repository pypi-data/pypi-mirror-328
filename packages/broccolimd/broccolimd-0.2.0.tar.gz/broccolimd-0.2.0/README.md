# broccolimd

[![PyPI - Version](https://img.shields.io/pypi/v/broccolimd.svg)](https://pypi.org/project/broccolimd)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/broccolimd.svg)](https://pypi.org/project/broccolimd)

Extract [Broccoli](https://github.com/flauschtrud/broccoli) backups as markdown notes.

-----

**Table of Contents**

- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Usage

`broccolimd` takes only one required argument: the path to the backup file that should be extracted.

```bash
broccolimd backups/broccoli/EXPORT_20250122_140251.broccoli-archive
```

### Options

While only one argument is required, there are a couple of options that can be provided:

- `--output-markdown-dir`: Directory path to export recipes to; Defaults to `./recipes`
- `--output-media-dir`: Directory path to export recipe attachments to; Defaults to `./recipes/media`

## Installation

```console
pip install broccolimd
```

### Install dev env

```console
pip install -e .[dev]
```

## License

`broccolimd` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
