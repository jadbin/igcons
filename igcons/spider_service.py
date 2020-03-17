# coding=utf-8

import requests
import json
from os.path import join

from guniflask.context import service
from guniflask.config import settings


@service
class SpiderService:

    def __init__(self):
        self.spider_service_address = settings['spider_service_address']
        self.spider_dir = settings['spider_dir']
        self.spider_result_file = settings['spider_result_file']
        pass

    def submit_spider_task(self, spider_name: str, spider_options: dict = None, callback: str = None) -> dict:
        data = {'spider_name': spider_name, 'spider_options': spider_options, 'callback': callback}
        response = requests.post('http://{}/api/submit-spider-task'.format(self.spider_service_address), json=data)
        return response.json()

    def get_spider_status(self, spider_token: str):
        # TODO
        pass

    def get_spider_result(self, spider_token: str):
        with open(join(self.path_utils.spider_result_dir(spider_token), self.spider_result_file), 'r') as f:
            data = json.load(f, ensure_ascii=False)
        return data




