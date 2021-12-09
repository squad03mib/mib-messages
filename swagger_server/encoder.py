from connexion.apps.flask_app import FlaskJSONEncoder
import six

from swagger_server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        return FlaskJSONEncoder.default(self, o)
