[![Build Status](https://travis-ci.com/Shadark/ClauseWizard.svg?branch=master)](https://travis-ci.com/Shadark/ClauseWizard) [![PyPI version](https://badge.fury.io/py/ClauseWizard.svg)](https://badge.fury.io/py/ClauseWizard) ![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)

# ClauseWizard
Python-based JSON parser for files from the Clausewitz engine, used in multiple Paradox Interactive games. You can open the resulting files with any text editor, but since the file size can exceed the allowed limit for some editors,  you can use other software such as [HugeJsonViewer](https://github.com/WelliSolutions/HugeJsonViewer).

Currently supports both savegames and files from:

* **Europa Universalis 4**
* **Crusader Kings 2**
* **Hearts of Iron 4**
* **Stellaris**

---

* Compressed games: **supported**.
* Multiplayer games: **supported**.
* Ironman games: _not supported_ (in development). If the ironman save is not in binary format, it should work with this library.
_(For HoI4 games, you need to change `save_as_binary=yes` option from `yes` to `no` on your `settings.txt` configuration file)._

# Getting started

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ClauseWizard.

```bash
pip install ClauseWizard
```

Binary packages are available for download in the [Release](https://github.com/Shadark/ClauseWizard/releases) page.

_Python version is 3.7, will test other versions._

## Usage

```python
import ClauseWizard

ClauseWizard.cwparse(file) # returns a list of tokens
ClauseWizard.cwformat(tokens) # returns a JSON-formatted string
```

You can also run `Scripts\CWParser` from your Python setup directory.

## Built With

* [PyParsing](https://github.com/pyparsing/pyparsing) - Parsing library

## Contributing
Pull requests are welcome, specially for performance upgrades, the current code takes too long to execute.

## Author(s)

* **Shadark** - [Shadark](https://github.com/Shadark)

[![Donate](https://az743702.vo.msecnd.net/cdn/kofi4.png)](https://ko-fi.com/shadark)

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE](LICENSE) file for details.



## Acknowledgments

* [Paradox Interactive](https://www.paradoxplaza.com/) for their great games & the creation of the Clausewitz engine.
* [Anthorath](https://forum.paradoxplaza.com/forum/index.php?members/anthorath.117345/) for being a good listener and not falling asleep while I explain all the code.
* to_be_filled.jpg

#### Disclaimer
_This site is not affiliated with Paradox Interactive or Clausewitz Engine.
All product names, trademarks and registered trademarks are property of their respective owners.
All company, product and service names used in this website are for identification purposes only._
