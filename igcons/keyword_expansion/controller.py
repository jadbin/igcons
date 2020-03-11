# coding=utf-8

from flask import request, jsonify

from guniflask.web import blueprint, get_route, post_route

from igcons.path_utils import PathUtils
from .service import KeywordExpansionService


@blueprint('/api')
class KeywordExpansionController:
    def __init__(self, path_utils: PathUtils, keyword_expansion_service: KeywordExpansionService):
        self.path_utils = path_utils
        self.keyword_expansion_service = keyword_expansion_service

    @post_route('/keyword-expansion/spider-service-callback')
    def spider_service_callback(self):
        task_token = request.args.get('task_token')
        self.keyword_expansion_service.recover_after_spider_service_callback(task_token)

    @post_route('/keyword-expansion/expasion-callback')
    def expand_callback(self):
        task_token = request.args.get('task_token')
        self.keyword_expansion_service.recover_after_expand_service_callback(task_token)

    @post_route('/keyword-expansion/manual-judge-callback')
    def manual_judge_callback(self):
        task_token = request.args.get('task_token')
        manual_judge_result = request.args.get('results')
        self.keyword_expandsion_service.recover_after_manual_judge_service_callback(task_token, manual_judge_result)



@blueprint('/submit')
class SubmitController:
    """
    用于接收各类任务提交的申请
    """

    def __init__(self, path_utils: PathUtils):
        self.path_utils = path_utils

    @post_route('/spider-task')
    def submit_spider_task(self):
        """
        用于接收爬虫任务的提交申请
        :return:
        """
        params = request.json
        # TODO: 从spider获取token
        params['spider_token'] = ''
        return params

    @post_route('/expand-task')
    def submit_expand_task(self):
        """
        用于接收关键词拓展任务的提交申请
        :return:
        """
        params = request.json
        # TODO: 从 expand 系统获取expand_token
        params['expand_token'] = ''
        return params

    @post_route('/manual-judge')
    def submit_manual_judge_task(self):
        """

        :return:
        """
        params = request.json
        # TODO: 从 人工研判系统获取 token
        params['judge_token'] = ''
        return params

