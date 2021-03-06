"""

Configuration module.

"""


class Config:
    """
    Basic environment configuration class
    """
    def __init__(self):
        self.TESTING = True
        self.FLASK_APP = 'app.py'
        self.FLASK_ENV = ''


class ProductionConfig(Config):
    """
    Production environment configuration class
    """
    def __init__(self):
        super().__init__()
        self.TESTING = False
        self.FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    """
    Development environment configuration class
    """
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.TESTING = True
        self.FLASK_ENV = 'development'


class TestingConfig(Config):
    """
    Testing environment configuration class
    """
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.TESTING = True
        self.FLASK_ENV = 'qa'


class FactoryConfigClass:
    """
    Factory Config class.
    Get configuration based on environment
    """
    def __init__(self, env):
        if env == "dev" or env == 'development':
            self.config = DevelopmentConfig()
        elif env == "qa" or env == "testing":
            self.config = TestingConfig()
        elif env == "prod" or env == "production":
            self.config = ProductionConfig()
        else:
            self.config = Config()
