# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
from typing import Union

from autohooks.api import out, ok, error
from autohooks.config import Config

DEFAULT_ROOT_DIR = 'tests'
DEFAULT_VIEW_MODE = '-v'
DEFAULT_COVERAGE_SOURCE = "src"
DEFAULT_COVERAGE_ON_FAIL = True
DEFAULT_COVERAGE_FAIL_UNDER = 100
DEFAULT_COVERAGE_REPORT_FORMAT = 'html'


def check_pytest_installed():
    try:
        import pytest  # pylint: disable=unused-import
    except ImportError:
        raise Exception(
            'Could not find pytest. Please add pytest to your python environment'
        )


def get_pytest_config(config: Config) -> Config:
    return config.get('tool', 'autohooks', 'plugins', 'pytest')


def get_source_from_config(config: Union[None, Config]) -> str:
    if not config:
        return DEFAULT_ROOT_DIR
    pytest_config = get_pytest_config(config)
    root_dir = pytest_config.get_value('root_dir', DEFAULT_ROOT_DIR)
    if isinstance(root_dir, str):
        return root_dir
    return root_dir


def get_view_mode_from_config(config: Union[None, Config]) -> str:
    if not config:
        return DEFAULT_VIEW_MODE
    pytest_config = get_pytest_config(config)
    view_mode = pytest_config.get_value('view_mode', DEFAULT_VIEW_MODE)
    if isinstance(view_mode, str):
        return view_mode
    return view_mode


def get_cov_source_from_config(config: Union[None, Config]) -> str:
    if not config:
        return DEFAULT_COVERAGE_SOURCE
    pytest_config = get_pytest_config(config)
    cov_source = pytest_config.get_value('cov_source', DEFAULT_COVERAGE_SOURCE)
    if isinstance(cov_source, str):
        return cov_source
    return cov_source


def get_cov_on_fail_from_config(config: Union[None, Config]) -> str:
    if not config:
        return DEFAULT_COVERAGE_ON_FAIL
    pytest_config: Config = get_pytest_config(config)
    cov_on_fail: bool = pytest_config.get_value(
        'cov_on_fail', DEFAULT_COVERAGE_ON_FAIL)
    cov_fail: str = ""
    if isinstance(cov_on_fail, bool):
        cov_on_fail = cov_on_fail
    if cov_on_fail is True:
        cov_fail = "--no-cov-on-fail"
    return cov_fail


def get_cov_fail_under_from_config(config: Union[None, Config]) -> int:
    if not config:
        return DEFAULT_COVERAGE_FAIL_UNDER
    pytest_config = get_pytest_config(config)
    cov_under_fail = pytest_config.get_value(
        'cov_under_fail', DEFAULT_COVERAGE_FAIL_UNDER)
    if isinstance(cov_under_fail, int):
        return cov_under_fail
    return cov_under_fail


def get_cov_report_format_from_config(config: Union[None, Config]) -> str:
    if not config:
        return DEFAULT_COVERAGE_REPORT_FORMAT
    pytest_config = get_pytest_config(config)
    cov_report_format = pytest_config.get_value(
        'cov_report_format', DEFAULT_COVERAGE_REPORT_FORMAT)
    if isinstance(cov_report_format, str):
        return cov_report_format
    return cov_report_format


def precommit(config=Union[None, Config], **kwargs) -> int:  # pylint: disable=unused-argument
    # out('Running pytest pre-commit hook')
    check_pytest_installed()
    root_dir = get_source_from_config(config)
    view_mode = get_view_mode_from_config(config)
    cov_source = get_cov_source_from_config(config)
    cov_on_fail = get_cov_on_fail_from_config(config)
    cov_fail_under = get_cov_fail_under_from_config(config)
    cov_report_format = get_cov_report_format_from_config(config)

    call_str = ["python", "-m", "pytest", "--tb=line", view_mode, "--rootdir", root_dir, "--cov",
                cov_source,  "--cov-fail-under", str(cov_fail_under), "--cov-report", cov_report_format, cov_on_fail]
    try:
        subprocess.check_call(call_str)
        ok('Running pytest on all test files')
    except subprocess.CalledProcessError as e:
        error('Running pytest get fail on some test cases')
        raise Exception("Some test cases got failed")
    return 0
