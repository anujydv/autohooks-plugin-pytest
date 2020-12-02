from pathlib import Path

import pytest
from autohooks.config import load_config_from_pyproject_toml, AutohooksConfig, Config

from autohooks.plugins.pytest.pytest import *


def get_test_config_path(
        name):
    return Path(
        __file__).parent / name


@pytest.fixture
def conf1() -> Config:
    config_path = get_test_config_path(
        'test_config_custom.toml')
    assert config_path.is_file()

    return load_config_from_pyproject_toml(config_path).get_config()


@pytest.fixture
def conf2() -> Config:
    config_path = get_test_config_path('test_config_default.toml')
    assert config_path.is_file()

    return load_config_from_pyproject_toml(config_path).get_config()


@pytest.fixture
def conf3() -> Config:
    config_path = get_test_config_path('test_config_3.toml')
    assert config_path.is_file()

    return load_config_from_pyproject_toml(config_path).get_config()


def test_source_from_config(conf1):
    assert 'api_test' == get_source_from_config(conf1)


def test_include_default(conf2):
    assert get_source_from_config(conf2) == "tests"


def test_view_mode_from_config(conf1):
    assert get_view_mode_from_config(conf1) == "-rf"


def test_view_mode_default(conf2):
    assert get_view_mode_from_config(conf2) == "-v"


def test_cov_source_from_config(conf1):
    assert get_cov_source_from_config(conf1) == "www"


def test_cov_source_default(conf2):
    assert get_cov_source_from_config(conf2) == "autohooks"


def test_cov_on_fail_from_config(conf1):
    assert get_cov_on_fail_from_config(conf1) == ""


def test_cov_on_fail_default(conf2):
    assert get_cov_on_fail_from_config(conf2) == "--no-cov-on-fail"

def test_cov_fail_under_from_config(conf1):
    assert get_cov_fail_under_from_config(conf1) == 80


def test_cov_fail_under_default(conf2):
    assert get_cov_fail_under_from_config(conf2) == 100

def test_cov_report_format_from_config(conf1):
    assert get_cov_report_format_from_config(conf1) == "xml"


def test_cov_report_format_default(conf2):
    assert get_cov_report_format_from_config(conf2) == "html"



