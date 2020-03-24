# coding=utf-8

import requests
from igcons.models.announce import Announce

from guniflask.context import service
from guniflask.config import settings
from igcons.app import db

@service
class JudgeService:

    def __init__(self):
        self.judge_service_address = settings['judge_service_address']

    def submit_judge_task(self, expand_result: list, judge_options: dict = None, callback: str = None) -> dict:

        # 发起人工研判的通知
        self.announce_notification(expand_result, judge_options, callback)
        # data = {'analyze_options': judge_options, 'callback': callback}
        # response = requests.post('http://{}/submit/judge-task'.format(self.judge_service_address), json=data)
        # return response.json()

    def announce_notification(self, expand_result: list, judge_options: dict = None, callback: str = None):
        """

        :param expand_result: [{keyword:---, context:---}, ...]
        :param judge_options:
        :param callback:
        :return:
        """
        # TODO: 向数据库写入一条 人工研判通知 的记录
        for item in expand_result:
            announce = Announce.from_dict(item, ignore='id')
            db.session.add(announce)

        db.session.commit()

    def save_judge_results(self, manual_judge_results):
        # TODO: 向数据库写入记录
        pass

    def get_judge_status(self, token: str) -> list:
        """

        :param token:
        :return:  返回的是 人工研判 得到的关键词列表 [{'word':---, 'key': ---}]
        """
        # TODO
        pass

    def get_judge_result(self, token: str):
        # TODO
        pass
