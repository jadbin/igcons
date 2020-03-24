# coding=utf-8

import requests
from os.path import join
import json
from flask import jsonify


from igcons.path_utils import PathUtils
from guniflask.context import service
from guniflask.config import settings

from igcons.app import db
from igcons.models.announce import Announce



@service('expand-judge-service')
class ExpandService:

    def __init__(self, path_utils: PathUtils):
        self.expand_service_address = settings['expand_service_address']
        self.path_utils = path_utils

    def submit_expand_task(self, spider_result, expand_options: dict = None, callback: str = None) -> dict:

        data = {'keywords': spider_result['keyword'], 'cleaned_text':spider_result['txt'], 'expand_options': expand_options, 'callback': callback}
        response = requests.post('http://{}/api/submit-expand-task'.format(self.expand_service_address), json=data)
        return response.json()

    def get_expand_status(self, expand_token: str):
        """
        """
        pass

    def get_expand_results(self, expand_token: str) -> list:
        """

        :param token:
        :return: 返回的是拓展得到的关键词列表 [{'word':---, 'key': ---}]
        """
        path = join(
            join(join(self.path_utils.expand_result_dir, expand_token), "result/", self.path_utils.spider_result_file))
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    def receive_judge_results(self, result: list):
        """
        获取用户研判合格的关键词列表，并存入图谱
        :param result:
        :return:
        """

        for item in result:
            print("########### item: ", item)
            line = Announce.query.filter_by(id=item['id']).update({'flag': item['flag'], 'judge_user':item['judge_user']})
            print("$$$$$$$$$$$$$$$$$$$$$$ ", line)
            # property_type.update_by_dict(item, ignore='id,clause,context,insert_time,judge_time')
        db.session.commit()

    def load_unjudge_keywords(self) -> list:
        """
        从数据库读取未研判的关键词
        :page_num: 每一页显示多少条记录
        :return:
        """

        items = Announce.query.filter_by(flag=False)
        d = [p.to_dict() for p in items]
        return d
