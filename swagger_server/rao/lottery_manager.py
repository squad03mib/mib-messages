from swagger_server import app
from swagger_server.models.lottery_info import LotteryInfo
from flask import abort
import requests
import json


class LotteryManager:
    LOTTERY_ENDPOINT = app.config['LOTTERY_MS_URL']
    REQUESTS_TIMEOUT_SECONDS = app.config['REQUESTS_TIMEOUT_SECONDS']

    @classmethod
    def get_lottery_by_id_user(cls, id_user: int):
        """
        This method contacts the lottery microservice
        and retrieves the lottery object by user id.
        :param id_user: the user id
        :return: Lottery obj with id_user=id_user
        """
        lottery_info :LotteryInfo = LotteryInfo()
        lottery_info.id = 0
        lottery_info.points = 0
        lottery_info.trials = 0
        if cls.LOTTERY_ENDPOINT is None:
            return lottery_info
        try:
            response = requests.get("%s/users/%s/lottery" % (cls.LOTTERY_ENDPOINT, str(id_user)),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)
            json_payload = response.json()

            if response.status_code == 200:
                lottery = json_payload
            else:
                raise RuntimeError(
                    'Server has sent an unrecognized status code %s' % response.status_code)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return lottery

    @classmethod
    def create_lottery(cls, id_user: int, points: int, trials: int, user_id :int):
        lottery_info :LotteryInfo = LotteryInfo()
        lottery_info.id = 0
        lottery_info.points = 0
        lottery_info.trials = 0
        if cls.LOTTERY_ENDPOINT is None:
            return lottery_info
        try:
            url = "%s/users/%s/lottery" % (cls.LOTTERY_ENDPOINT,
                                           str(user_id))
            response = requests.post(url,
                                     json={
                                         'id_user': id_user,
                                         'points': points,
                                         'trials': trials
                                     },
                                     timeout=cls.REQUESTS_TIMEOUT_SECONDS
                                     )

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return response

    @classmethod
    def update_lottery(cls, id_user: int, points: int, trials: int, user_id : int):
        lottery_info :LotteryInfo = LotteryInfo()
        lottery_info.id = 0
        lottery_info.points = 0
        lottery_info.trials = 0
        if cls.LOTTERY_ENDPOINT is None:
            return lottery_info
        try:
            url = "%s/users/%s/lottery" % (cls.LOTTERY_ENDPOINT,
                                           str(user_id))
            response = requests.post(url,
                                     json={
                                         'id_user': id_user,
                                         'points': points,
                                         'trials': trials
                                     },
                                     timeout=cls.REQUESTS_TIMEOUT_SECONDS
                                     )

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return abort(500)

        return response
