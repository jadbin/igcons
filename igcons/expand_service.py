# coding=utf-8

import requests

from guniflask.context import service
from guniflask.config import settings


@service('expand-judge-service')
class ExpandService:

    def __init__(self):
        self.expand_service_address = settings['expand_service_address']
        pass

    def submit_expand_task(self, spider_result, expand_options: dict = None, callback: str = None) -> dict:

        data = {'keywords': spider_result['keyword'], 'cleaned_text':spider_result['txt'], 'expand_options': expand_options, 'callback': callback}
        response = requests.post('http://{}/api/submit-expand-task'.format(self.expand_service_address), json=data)
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

    def receive_judge_results(self, result: list):
        """
        获取用户研判合格的关键词列表，并存入图谱
        :param result:
        :return:
        """
        print("receive_judge_results ...")
        pass

    def load_unjudge_keywords(self, load_num) -> list:
        """
        从数据库读取未研判的关键词
        :page_num: 每一页显示多少条记录
        :return:
        """
        print("load_unjudge_keywords ...")
        unjudge_keywords = ['a', 'b', 'c']
        return unjudge_keywords
