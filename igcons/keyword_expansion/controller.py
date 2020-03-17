# coding=utf-8

from flask import request, jsonify

from guniflask.web import blueprint, get_route, post_route

from igcons.path_utils import PathUtils
from .service import KeywordExpansionService

from igcons.spider_service import SpiderService
from igcons.expand_service import ExpandService
from igcons.judge_service import JudgeService
from igcons.task_context import TaskContext, TaskContextService


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

    @post_route('/trigger')
    def trigger(self):
        spider_name = request.json['spider_name']
        keyword = request.json['spider_name']
        self.keyword_expansion_service.start_keyword_expansion(keyword=keyword, spider_name=spider_name)
