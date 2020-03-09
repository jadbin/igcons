# coding=utf-8

from flask import request

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
