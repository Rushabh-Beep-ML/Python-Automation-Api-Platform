import os
from datetime import timedelta

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', True)
    TESTING = False

    API_TIMEOUT = int(os.getenv('API_TIMEOUT', 10))
    MAX_INPUT_SIZE = int(os.getenv('MAX_INPUT_SIZE', 1000000))

    EXTERNAL_API_BASE_URL = os.getenv('EXTERNAL_API_BASE_URL', 'https://jsonplaceholder.typicode.com')

    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    API_TIMEOUT = 5
