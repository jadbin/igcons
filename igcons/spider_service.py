# coding=utf-8

import requests

from guniflask.context import service
from guniflask.config import settings


@service
class SpiderService:

    def __init__(self):
        self.spider_service_address = settings['spider_service_address']
        pass

    def submit_spider_task(self, spider_name: str, spider_options: dict = None, callback: str = None) -> dict:

        data = {'spider_name': spider_name, 'spider_options': spider_options, 'callback': callback}
        response = requests.post('http://{}/submit/spider-task'.format(self.spider_service_address), json=data)
        return response.json()

    def get_spider_status(self, token: str):
        # TODO
        pass

    def get_spider_result(self, token: str):
        # TODO
        pass
