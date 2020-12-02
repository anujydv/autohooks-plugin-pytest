# autohooks-plugin-pytest[![Build Status](https://travis-ci.com/anujydv/autohooks-plugin-pytest.svg?branch=master)](https://travis-ci.com/anujydv/autohooks-plugin-pytest)

An [autohooks](https://github.com/greenbone/autohooks) plugin for python code
testing via [pytest](https://github.com/pytest-dev/pytest).

## Installation

### Install using pip

You can install the latest stable release of autohooks-plugin-pytest from the
Python Package Index using [pip](https://pip.pypa.io/):

    pip install autohooks-plugin-pytest

Note the `pip` refers to the Python 3 package manager. In a environment where
Python 2 is also available the correct command may be `pip3`.

### Install using pipenv

It is highly encouraged to use [pipenv](https://github.com/pypa/pipenv) for
maintaining your project's dependencies. Normally autohooks-plugin-pytest is
installed as a development dependency.

    pipenv install --dev autohooks-plugin-pytest

## Usage

To activate the pytest autohooks plugin please add the following setting to your
`pyproject.toml` file.

````toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pytest"]
````
### Customizing the `pytest` behavior

To pass options to `pytest`, you have to add an additional
````toml
[tool.autohooks.plugins.pytest]
option = "value"
````

block to your `pyproject.toml` file. Possible options are explained in the following.
* #### Update root dir
    By default, autohooks plugin pytest checks all files with a "test_*.py" inside tests directory . To update root directory just add the following setting:

    ````toml
    root_dir = "api_test"
    ````
* #### Select different view mode

    You can update the pytest `cli` view mode. some modes are : </br>
    * quite `"-q"`
    * non-verbose `"-rf"`

    ````toml
    view_mode = "-q"
    ````

    default mode `"-v"` verbose.

* #### Set coverage source
    You have to update the coverage directory : </br>
    ````toml
    cov_source = "src"
    ````

    default direcotry is `"src"` .
* #### Set coverage on pytest fail
    You can update the coverage on pytest fail : </br>
    ````toml
    cov_on_fail = false
    ````

    default value is `true` .
* #### Set coverage under fail
    You can update the coverage  : </br>
    ````toml
    cov_under_fail = 80
    ````

    default percentage is `100` .
* #### Set coverage report format
    You can update the coverage report format : </br>
    ````toml
    cov_report_format = "html"
    ````

    default report format is `"xml"` .

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/anujydv/autohooks-plugin-pytest/pulls)
on GitHub. Bigger changes need to be discussed with the development team via the
[issues section at GitHub](https://github.com/anujydv/autohooks-plugin-pytest/issues)
first.

## License

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
