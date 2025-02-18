# **$\color{#8085FF}\Huge\textsf{XulbuX}$**

**$\color{#8085FF}\textsf{XulbuX}$** is a library which includes a lot of really helpful classes, types and functions.

For precise information about the library, see the library's [Wiki page](https://github.com/XulbuX/PythonLibraryXulbuX/wiki).<br>
For the libraries latest changes, see the [change log](https://github.com/XulbuX/PythonLibraryXulbuX/blob/main/CHANGELOG.md).


## Installation

To install the library and all its dependencies, open a console and run the command:
```prolog
pip install xulbux
```

To upgrade the library to the latest available version, run the following command in your console:
```prolog
pip install --upgrade xulbux
```


## Usage

Import the full library under the alias `xx`, so it's classes, types and functions are accessible with `xx.Class.method()`, `xx.type()` and `xx.function()`:
```python
import xulbux as xx
```
So you don't have to write `xx` in front of the library's types, you can import them directly:
```python
from xulbux import rgba, hsla, hexa
```


# Modules

| | |
| :--------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------- |
| <h3>[`xx_code`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_code)</h3>                 | advanced code-string operations (*changing the indent, finding function calls, ...*)               |
| <h3>[`xx_color`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_color)</h3>               | everything around colors (*converting, blending, searching colors in strings, ...*)                |
| <h3>[`xx_console`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_console)</h3>           | advanced actions related to the console (*pretty logging, advanced inputs, ...*)                   |
| <h3>[`xx_data`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_data)</h3>                 | advanced operations with data structures (*compare, generate path ID's, pretty print/format, ...*) |
| <h3>[`xx_env_path`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_env_path)</h3>         | getting and editing the PATH variable (*get paths, check for paths, add paths, ...*)               |
| <h3>[`xx_file`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_file)</h3>                 | advanced working with files (*create files, rename file-extensions, ...*)                          |
| <h3>[`xx_format_codes`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_format_codes)</h3> | easy pretty printing with custom format codes (*print, inputs, custom format codes to ANSI, ...*)  |
| <h3>`xx_json`</h3>                                                                                   | advanced working with json files (*read, create, update, ...*)                                     |
| <h3>`xx_path`</h3>                                                                                   | advanced path operations (*get paths, smart-extend relative paths, delete paths, ...*)             |
| <h3>`xx_regex`</h3>                                                                                  | generated regex pattern-templates (*match bracket- and quote pairs, match colors, ...*)            |
| <h3>[`xx_string`](https://github.com/XulbuX/PythonLibraryXulbuX/wiki/xx_string)</h3>             | helpful actions when working with strings. (*normalize, escape, decompose, ...*)                   |
| <h3>`xx_system`</h3>                                                                                 | advanced system actions (*restart with message, check installed Python libs, ...*)                 |


<br>

--------------------------------------------------------------
[View this library on PyPI](https://pypi.org/project/XulbuX/)
