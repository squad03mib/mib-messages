#!/usr/bin/env python3

import os

__version__ = '0.1'

import connexion
from swagger_server import encoder
from flask_sqlalchemy import SQLAlchemy
from flask_environments import Environments

db = None
app = None
api_app = None


def create_app():

    global db
    global app
    global api_app

    api_app = connexion.FlaskApp(
        __name__,
        server='flask',
        specification_dir='./swagger/'
    )
    app = api_app.app
    app.json_encoder = encoder.JSONEncoder
    api_app.add_api('swagger.yaml', arguments={
        'title': 'Message Service API'}, pythonic_params=True)

    flask_env = os.getenv('FLASK_ENV', 'None')
    if flask_env == 'development':
        config_object = 'config.DevConfig'
    elif flask_env == 'testing':
        config_object = 'config.TestConfig'
    elif flask_env == 'production':
        config_object = 'config.ProdConfig'
    else:
        raise RuntimeError(
            '%s is not recognized as valid app environment. You have to setup the environment!' % flask_env
        )

    env = Environments(app)
    env.from_object(config_object)

    db = SQLAlchemy(
        app=app
    )

    assert db != None

    if flask_env == 'testing':
        db.create_all()

    return app


if __name__ == '__main__':
    create_app().run(port=8080)
