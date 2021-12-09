from swagger_server import app
from swagger_server.models.lottery_info import LotteryInfo
from swagger_server.models.points import Points
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
        lottery_info :LotteryInfo = None
        if cls.LOTTERY_ENDPOINT is None:
            lottery_info = LotteryInfo()
            lottery_info.id = 0
            lottery_info.points = 0
            lottery_info.trials = 0
            return lottery_info
        try:
            response = requests.get("%s/users/%s/lottery" % (cls.LOTTERY_ENDPOINT, str(id_user)),
                                    timeout=cls.REQUESTS_TIMEOUT_SECONDS)

            if response.status_code == 200:
                lottery_info = LotteryInfo.from_dict(response.json())
            elif response.status_code != 404:
                return abort(500)

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(e)
            return abort(500)

        return lottery_info
    

    @classmethod
    def spend_lottery_points_by_id_user(cls, id_user :int, points_to_spend :int):
        """
        This method contacts the lottery microservice
        and retrieves the lottery object by user id.
        :param id_user: the user id
        :return: Lottery obj with id_user=id_user
        """
        points :Points = Points()
        points.count = points_to_spend
        try:
            response = requests.post("%s/users/%s/lottery/use" % (cls.LOTTERY_ENDPOINT, str(id_user)),
                                     json=points.to_dict(), timeout=cls.REQUESTS_TIMEOUT_SECONDS)
            if response.status_code == 200:
                return True
            else:
                return False

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(e)
            return abort(500)
