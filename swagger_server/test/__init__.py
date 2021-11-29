import logging

import connexion
import unittest

from swagger_server.encoder import JSONEncoder
from swagger_server import create_app


class BaseTestCase(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests resources
    """
    client = None

    @classmethod
    def setUpClass(cls):
        from swagger_server import create_app
        app = create_app()
        cls.client = app.test_client()
