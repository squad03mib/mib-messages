class Config(object):
    DEBUG = False
    TESTING = False
    import os
    USERS_MS_URL = os.getenv('USERS_MS_URL', None)
    REQUESTS_TIMEOUT_SECONDS = os.getenv('REQUESTS_TIMEOUT_SECONDS', None)


class DebugConfig(Config):
    '''
    This is the main configuration object ofr the app.
    '''
    DEBUG = True
    TESTING = False

    SECRET_KEY = b'isreallynotsecret'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(DebugConfig):
    '''
    This is the main configuration object ofr the app.
    '''
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    '''
    This is the main configuration object ofr the app.
    '''
    TESTING = True

    import os
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(DevConfig):
    '''
    This is the main configuration object of the app.
    '''
    DEBUG = False
    TESTING = False

    import os
    SECRET_KEY = os.getenv('APP_SECRET_KEY', os.urandom(24))

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_USER = os.getenv('POSTGRES_USER', None)
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)
    POSTGRES_DB = os.getenv('POSTGRES_DB', None)
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', None)
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
