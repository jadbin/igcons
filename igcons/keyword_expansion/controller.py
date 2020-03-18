# coding=utf-8

from flask import request, current_app, jsonify

from guniflask.web import blueprint, get_route, post_route

from igcons.path_utils import PathUtils
from .service import KeywordExpansionService

from igcons.spider_service import SpiderService
from igcons.expand_service import ExpandService
from igcons.judge_service import JudgeService
from igcons.task_context import TaskContext, TaskContextService

from guniflask.context import BeanContext


@blueprint('/api')
class KeywordExpansionController:
    def __init__(self, path_utils: PathUtils, keyword_expansion_service: KeywordExpansionService):
        self.path_utils = path_utils
        self.keyword_expansion_service = keyword_expansion_service

    @post_route('/keyword-expansion/spider-service-callback')
    def spider_service_callback(self):
        task_token = request.args.get('task_token')
        self.keyword_expansion_service.recover_after_spider_service_callback(task_token)
        return jsonify({'code': 200})

    @post_route('/keyword-expansion/expansion-callback')
    def expand_callback(self):
        task_token = request.args.get('task_token')
        self.keyword_expansion_service.recover_after_expand_service_callback(task_token)

    @post_route('/keyword-expansion/manual-judge-callback')
    def manual_judge_callback(self):
        task_token = request.args.get('task_token')
        manual_judge_result = request.args.get('results')
        self.keyword_expandsion_service.recover_after_manual_judge_service_callback(task_token, manual_judge_result)

    @post_route('/trigger')
    def trigger(self):
        spider_name = request.json['spider_name']
        keyword = request.json['keyword']
        self.keyword_expansion_service.start_keyword_expansion(keyword=keyword, spider_name=spider_name)
        return jsonify({"code": 200})
#
# @blueprint('/front')
# class KeywordExpansionController:
#     def __init__(self, path_utils: PathUtils, expansion_service: ExpandService):
#         self.path_utils = path_utils
#         self.expand_service = expansion_service
#
#         self.expand_judge_service_bean_name = 'expand-judge-service'
#         self.receive_judge_result_method = 'receive_judge_results'
#         self.load_unjudge_keywords_method = 'load_unjudge_keywords'
#
#     @post_route('/judge')
#     def receive_judge_result(self):
#         """
#         接收前端用户研判为合格的关键词列表
#         request.json['result']: [{'keyword':--, 'provision':--, 'context':--, 'key':--, ...}, ..., ... ]
#         :return:
#         """
#         results = request.args.get('result')
#         bean_context = current_app.bean_context
#         assert isinstance(bean_context, BeanContext)
#         obj = bean_context.get_bean(self.expand_judge_service_bean_name)
#         method = getattr(obj, self.receive_judge_result_method)
#         method(results)
#         return 'receive judge result'
#
#     @post_route('/load_unjudge_keywords')
#     def load_unjudge_keywords(self):
#         """
#         查询未进行研判的关键词数据
#         :return:
#         """
#         load_num = request.args.get('load_num') # 加载数量
#         bean_context = current_app.bean_context
#         assert isinstance(bean_context, BeanContext)
#         obj = bean_context.get_bean(self.expand_judge_service_bean_name)
#         method = getattr(obj, self.load_unjudge_keywords_method)
#         unjudge_keywords = method(load_num)
#         return jsonify(unjudge_keywords)
