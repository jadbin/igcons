# coding=utf-8

import requests

from guniflask.context import service
from guniflask.config import settings


@service
class ExpandService:

    def __init__(self):
        self.expand_service_address = settings['expand_service_address']
        pass

    def submit_expand_task(self, spider_results: str, expand_options: dict = None, callback: str = None) -> dict:

        data = {'spider_results': spider_results, 'expand_options': expand_options, 'callback': callback}
        response = requests.post('http://{}/submit/expand-task'.format(self.expand_service_address), json=data)
        return response.json()

    def get_expand_status(self, token: str):
        """
        """
        pass

    def get_expand_results(self, token: str) -> list:
        """

        :param token:
        :return: 返回的是拓展得到的关键词列表 [{'word':---, 'key': ---}]
        """
        # TODO
        pass
