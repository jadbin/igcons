from guniflask.context import service
from guniflask.config import settings

from igcons.spider_service import SpiderService
from igcons.expand_service import ExpandService
from igcons.judge_service import JudgeService
from igcons.keyword_expansion.service import KeywordExpansionService
from igcons.task_context import TaskContext, TaskContextService


@service
class KeywordExpansionModelService:
    def __init__(self):
        pass


@service
class TestKeywordExpansionService:
    def __init__(self, general_service: KeywordExpansionService,
                 task_context_service: TaskContextService):

        self.general_service = general_service
        self.task_context_service = task_context_service


    # def test_submit_spider_task():
    #     data = {
    #             'method': 'spider', # ['spider', 'ES']
    #             'spider_name': 'baidu', # ['baidu', 'google', 'bing', 'general']
    #             'callback': url,
    #             'spider_options': {'keyword':'图谱'}
    #             }

    def test_start_keyword_expansion(self):

        keyword = '图谱'
        spider_name = 'baidu'
        options = None
        self.general_service.start_keyword_expansion(keyword, spider_name, options)
        

    def test_start_expand_words(self):

        # task_context = {'spider_token': 'faff826c53d04842acbd7b01bdbf72d7',
        #                 'expand_token': '27f228b3a4c7458bb88631fcac0df01b',
        #                 'callback': 'http://localhost:8068/api/keyword-expansion/expansion-callback?task_token=3a10dcaa-4da9-417f-b0c2-5169f2a91f71'}
        
        task_token = '3a10dcaa-4da9-417f-b0c2-5169f2a91f71'
        task_context = self.task_context_service.awake(task_token)
        task_context = self.general_service.start_expand_keywords(task_context)


    