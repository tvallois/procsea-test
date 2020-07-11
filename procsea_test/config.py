import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROCSEA_TEST_DB")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROCSEA_TEST_DB_TEST")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    pass
