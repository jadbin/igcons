# coding=utf-8

from guniflask.context import service
from guniflask.config import settings

from igcons.spider_service import SpiderService
from igcons.task_context import TaskContext, TaskContextService


@service
class KeywordExpansionModelService:
    def __init__(self):
        pass


@service
class KeywordExpansionService:
    def __init__(self, spider_service: SpiderService, task_context_service: TaskContextService):
        self.spider_service = spider_service
        self.task_context_service = task_context_service

    def start_keyword_expansion(self, keyword, options: dict = None):
        # FIXME
        task_context = TaskContext()

        callback = 'http://{}/api/keyword-expansion/spider-service-callback?task_token={}'.format(
            settings['server_address'], task_context.token)
        spider_name = ''
        spider_options = {}
        spider_task = self.spider_service.submit_spider_task(spider_name,
                                                             spider_options=spider_options,
                                                             callback=callback)

        task_context['spider_token'] = spider_task.get('token')

        self.task_context_service.suspend(task_context)

    def recover_after_spider_service_callback(self, task_token):
        task_context = self.task_context_service.awake(task_token)
        # TODO: 异步运行 analyze_spider_result(task_context)
        pass

    def analyze_spider_result(self, task_context):
        # TODO
        spider_result = self.spider_service.get_spider_result(task_context['spider_token'])

        pass
