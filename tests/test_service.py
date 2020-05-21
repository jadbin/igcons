from guniflask.context import service
from guniflask.config import settings

from igcons.spider_service import SpiderService
from igcons.expand_service import ExpandService
from igcons.judge_service import JudgeService
from igcons.task_context import TaskContext, TaskContextService


@service
class KeywordExpansionModelService:
    def __init__(self):
        pass


@service
class TestService:
    def __init__(self, spider_service: SpiderService,
                 expand_service: ExpandService,
                 judge_service: JudgeService,
                 task_context_service: TaskContextService):

        self.spider_service = spider_service
        self.expand_service = expand_service
        self.judge_service = judge_service # 人工研判
        self.task_context_service = task_context_service

    def test_submit_spider_task():

        spider_name = ''
        spider_options = ''
        callback = ''
        resp_data = self.spider_service.submit_spider_task(self, spider_name: str, spider_options: dict = None, callback: str = None)
        assert resp_data[xxx] == xxx

    def test_get_spider_result():

        spider_token = ''
        res = self.spider_service.get_spider_result(self, spider_token: str)
        # res不为空
        assert (res and isinstance(res, list))

    def test_submit_expand_task(self):

        spider_result = []
        expand_options = {}
        callback = ''
        resp_data = self.expand_service.submit_expand_task(spider_result, expand_options: dict = None, callback: str = None)
        assert resp_data[xxx] == xxx

    def test_get_expand_results(self):

        expand_token = ''
        res = self.expand_service.get_expand_results(expand_token)
        assert (res and isinstance(res, list))
        

    def test_start_expand_words(self, task_context):   
        task_token = ''
        task_context = self.task_context_service.awake(task_token)
        task_context = self.service.start_expand_keywords(task_context)


    