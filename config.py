class Config(object):
    DEBUG = False
    TESTING = False
    import os
    REQUESTS_TIMEOUT_SECONDS = int(os.getenv('REQUESTS_TIMEOUT_SECONDS', 10))

    # users microservice
    USERS_MS_PROTO = os.getenv('USERS_MS_PROTO', 'http')
    USERS_MS_HOST = os.getenv('USERS_MS_HOST', 'localhost')
    USERS_MS_PORT = os.getenv('USERS_MS_PORT', 5001)
    USERS_MS_URL = '%s://%s:%s' % (USERS_MS_PROTO,
                                   USERS_MS_HOST, USERS_MS_PORT)

    # content filter microservice
    CONTENT_FILTER_MS_PROTO = os.getenv('CONTENT_FILTER_MS_PROTO', 'http')
    CONTENT_FILTER_MS_HOST = os.getenv('CONTENT_FILTER_MS_HOST', 'localhost')
    CONTENT_FILTER_MS_PORT = os.getenv('CONTENT_FILTER_MS_PORT', 5005)
    CONTENT_FILTER_MS_URL = '%s://%s:%s' % (CONTENT_FILTER_MS_PROTO,
                                            CONTENT_FILTER_MS_HOST, CONTENT_FILTER_MS_PORT)

    # lottery microservice
    LOTTERY_MS_PROTO = os.getenv('LOTTERY_MS_PROTO', 'http')
    LOTTERY_MS_HOST = os.getenv('LOTTERY_MS_HOST', 'localhost')
    LOTTERY_MS_PORT = os.getenv('LOTTERY_MS_PORT', 5002)
    LOTTERY_MS_URL = '%s://%s:%s' % (LOTTERY_MS_PROTO,
                                     LOTTERY_MS_HOST, LOTTERY_MS_PORT)


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

    REQUESTS_TIMEOUT_SECONDS = 0
    USERS_MS_URL = None
    LOTTERY_MS_URL = None
    CONTENT_FILTER_MS_URL = None


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
