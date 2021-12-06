
from datetime import date
from swagger_server.models.user import User
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
        user :User = User()
        user.id = 1
        user.firstname = "Mario"
        user.lastname = "Rossi"
        user.email = "example@example.com"
        user.date_of_birth = date.fromisoformat('2001-01-01')
        user.is_active = True
        if cls.USERS_ENDPOINT is None:
            return user
        try:
            response = requests.get("%s/users/%s" % (cls.USERS_ENDPOINT, str(user_id)),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)
            json_payload = response.json()
            if response.status_code == 200:
                # user is authenticated
                user = User.build_from_json(json_payload)
                print("risposta: ",user)
            else:
                raise RuntimeError('Server has sent an unrecognized status code %s' % response.status_code)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return user

    @classmethod
    def get_user_by_email(cls, user_email: str):
        """
        This method contacts the users microservice
        and retrieves the user object by user email.
        :param user_email: the user email
        :return: User obj with email=user_email
        """
        user :User = User()
        user.id = 1
        user.firstname = "Mario"
        user.lastname = "Rossi"
        user.email = "example@example.com"
        user.date_of_birth = date.fromisoformat('2001-01-01')
        user.is_active = True
        if cls.USERS_ENDPOINT is None:
            return user
        try:
            response = requests.get("%s/user_email/%s" % (cls.USERS_ENDPOINT, user_email),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)
            json_payload = response.json()
            user = None

            if response.status_code == 200:
                user = User.build_from_json(json_payload)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return user

    @classmethod
    def create_user(cls,
                    email: str, password: str,
                    firstname: str, lastname: str,
                    birthdate):
        user :User = User()
        user.id = 1
        user.firstname = "Mario"
        user.lastname = "Rossi"
        user.email = "example@example.com"
        user.date_of_birth = date.fromisoformat('2001-01-01')
        user.is_active = True
        if cls.USERS_ENDPOINT is None:
            return user
        try:
            url = "%s/users" % cls.USERS_ENDPOINT
            response = requests.post(url,
                                     json={
                                         'email': email,
                                         'password': password,
                                         'firstname': firstname,
                                         'lastname': lastname,
                                         'birthdate': birthdate,
                                     },
                                     timeout=cls.REQUESTS_TIMEOUT_SECONDS
                                     )

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return response

    @classmethod
    def update_user(cls, user_id: int, email: str, password: str, phone: str):
        """
        This method contacts the users microservice
        to allow the users to update their profiles
        :param phone:
        :param password:
        :param email:
        :param user_id: the customer id
            email: the user email
            password: the user password
            phone: the user phone
        :return: User updated
        """
        user :User = User()
        user.id = 1
        user.firstname = "Mario"
        user.lastname = "Rossi"
        user.email = "example@example.com"
        user.date_of_birth = date.fromisoformat('2001-01-01')
        user.is_active = True
        if cls.USERS_ENDPOINT is None:
            return user
        try:
            url = "%s/users/%s" % (cls.USERS_ENDPOINT, str(user_id))
            response = requests.put(url,
                                    json={
                                        'email': email,
                                        'password': password
                                    },
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS
                                    )
            return response

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        raise RuntimeError('Error with searching for the user %s' % user_id)

    @classmethod
    def delete_user(cls, user_id: int):
        """
        This method contacts the users microservice
        to delete the account of the user
        :param user_id: the user id
        :return: User updated
        """
        if cls.USERS_ENDPOINT is None:
            return
        try:
            logout_user()
            url = "%s/users/%s" % (cls.USERS_ENDPOINT, str(user_id))
            response = requests.delete(url, timeout=cls.REQUESTS_TIMEOUT_SECONDS)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return response

    @classmethod
    def authenticate_user(cls, email: str, password: str) -> User:
        """
        This method authenticates the user trough users AP
        :param email: user email
        :param password: user password
        :return: None if credentials are not correct, User instance if credentials are correct.
        """
        user :User = User()
        user.id = 1
        user.firstname = "Mario"
        user.lastname = "Rossi"
        user.email = "example@example.com"
        user.date_of_birth = date.fromisoformat('2001-01-01')
        user.is_active = True
        if cls.USERS_ENDPOINT is None:
            return user
        payload = dict(email=email, password=password)
        try:
            print('trying response....')
            response = requests.post('%s/authenticate' % cls.USERS_ENDPOINT,
                                     json=payload,
                                     timeout=cls.REQUESTS_TIMEOUT_SECONDS
                                     )
            print('received response....')
            json_response = response.json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            # We can't connect to Users MS
            return abort(500)

        if response.status_code == 401:
            # user is not authenticated
            return None
        elif response.status_code == 200:
            user = User.build_from_json(json_response['user'])
            return user
        else:
            raise RuntimeError(
                'Microservice users returned an invalid status code %s, and message %s'
                % (response.status_code, json_response['error_message'])
            )
