
from datetime import date
import json
from typing import List
from swagger_server.models.user import User
from swagger_server.models.black_list_item import BlackListItem
from swagger_server import app
from flask import abort
import requests


class UserManager:
    USERS_ENDPOINT = app.config['USERS_MS_URL']
    REQUESTS_TIMEOUT_SECONDS = app.config['REQUESTS_TIMEOUT_SECONDS']

    @classmethod
    def get_user_by_id(cls, user_id: int) -> User:
        """
        This method contacts the users microservice
        and retrieves the user object by user id.
        :param user_id: the user id
        :return: User obj with id=user_id
        """
        user :User = None
        if cls.USERS_ENDPOINT is None:
            user = User()
            user.id = 1
            user.firstname = "Mario"
            user.lastname = "Rossi"
            user.email = "example@example.com"
            user.date_of_birth = date.fromisoformat('2001-01-01')
            user.is_active = True
            return user
        try:
            response = requests.get("%s/users/%s" % (cls.USERS_ENDPOINT, str(user_id)),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)

            if response.status_code == 200:
                user = User.from_dict(response.json())
            elif response.status_code != 404:
                return abort(500)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return user

    @classmethod
    def get_blacklist(cls, user_id: int):
        black_list :List[BlackListItem] = []
        if cls.USERS_ENDPOINT is None:
            black_list_item :BlackListItem = BlackListItem()
            black_list_item.id_user = user_id
            black_list_item.id_blacklisted = 2
            return [black_list_item]
        try:
            url = "%s/users/%s/blacklist" % (cls.USERS_ENDPOINT,
                                             user_id)
            response = requests.get(url, timeout=cls.REQUESTS_TIMEOUT_SECONDS)

            if response.status_code == 200:
                for item in response.json():
                    black_list_item :BlackListItem = BlackListItem.from_dict(item)
                    print(item)
                    black_list.append(black_list_item)
            elif response.status_code != 404:
                return abort(500)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return black_list
