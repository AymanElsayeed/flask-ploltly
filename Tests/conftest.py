"""
Configuration test fixture functions
"""
from src.config import FactoryConfigClass
from pytest import fixture
import app


def pytest_addoption(parser):
    """
    pytest add option to get params
    :param parser:
    :return:
    """
    parser.addoption("--env", action="store", help="environment to ru tests against")


def get_config_class(env):
    """
    Get configuration class
    :param env:
    :return:
    """
    return FactoryConfigClass(env).config


@fixture(scope="session")
def env(request):
    """
    Get env name
    :param request:
    :return:
    """
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    """
    Get app configuration
    :param env:
    :return:
    """
    return get_config_class(env=env)


@fixture(scope="session")
def get_api_client(env):
    """
    Flask api client for testing.
    :param env:
    :return:
    """
    run_env = get_config_class(env=env)
    app.app.config.update(run_env.__dict__)
    api = app.app.test_client()
    return api
