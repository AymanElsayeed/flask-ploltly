import pytest
from src.config import FactoryConfigClass


@pytest.mark.cfg
@pytest.mark.parametrize("env_name", ['development', 'qa', 'production'])
def test_config(env_name):
    config = FactoryConfigClass(env=env_name)
    assert config.config.FLASK_ENV == env_name


@pytest.mark.cfg
def test_env_name(app_config):
    assert app_config.FLASK_ENV in ["development", "qa", "production", '']
