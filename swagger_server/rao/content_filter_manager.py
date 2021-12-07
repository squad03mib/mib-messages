
from datetime import date
import json
from typing import List
from swagger_server.models.purify_message import PurifyMessage
from swagger_server import app
from flask import abort
import requests


class ContentFilterManager:
    CONTENT_FILTER_ENDPOINT = app.config['CONTENT_FILTER_MS_URL']
    REQUESTS_TIMEOUT_SECONDS = app.config['REQUESTS_TIMEOUT_SECONDS']

    @classmethod
    def purify_message(cls, user_id :int, msg: PurifyMessage) -> PurifyMessage:
        """
        This method contacts the users microservice
        and retrieves the user object by user id.
        :param user_id: the user id
        :return: User obj with id=user_id
        """
        purified_msg :PurifyMessage = None
        if cls.CONTENT_FILTER_ENDPOINT is None:
            purified_msg = PurifyMessage()
            purified_msg.text = msg.text
            return purified_msg
        try:
            response = requests.post("%s/users/%s/content_filter/purify_message" % (cls.CONTENT_FILTER_ENDPOINT, user_id),
                                    json=msg.to_dict(),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)

            if response.status_code == 200:
                purified_msg = PurifyMessage.from_dict(response.json())
                print(purified_msg.to_dict())
            elif response.status_code != 404:
                return abort(500)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return purified_msg
