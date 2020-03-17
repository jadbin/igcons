# coding=utf-8

from guniflask.context import service
from guniflask.config import settings

from igcons.spider_service import SpiderService
from igcons.expand_service import  ExpandService
from igcons.judge_service import JudgeService
from igcons.task_context import TaskContext, TaskContextService


@service
class KeywordExpansionModelService:
    def __init__(self):
        pass


@service
class KeywordExpansionService:
    def __init__(self, spider_service: SpiderService,
                 expand_service: ExpandService,
                 judge_service: JudgeService,
                 task_context_service: TaskContextService):

        self.spider_service = spider_service
        self.expand_service = expand_service
        self.judge_service = judge_service # 人工研判

        self.task_context_service = task_context_service

    def start_keyword_expansion(self, keyword: str, spider_name: str, options: dict = None):
        """
        采集接口
        :param keyword:
        :param options:
        :return:
        """

        task_context = TaskContext()

        callback = 'http://{}/api/keyword-expansion/spider-service-callback?task_token={}'.format(
            settings['server_address'], task_context.token)
        spider_options = {'keyword': keyword}
        spider_task = self.spider_service.submit_spider_task(spider_name=spider_name,
                                                             spider_options=spider_options,
                                                             callback=callback)

        task_context['spider_token'] = spider_task['spider_token']
        self.task_context_service.suspend(task_context)

    def recover_after_spider_service_callback(self, task_token):
        task_context = self.task_context_service.awake(task_token)
        # TODO: 异步运行 expand_keywords(task_context)
        self.start_expand_keywords(task_context)
        pass

    def start_expand_keywords(self, task_context):
        """
        获取爬虫数据采集的结果，将 关键词拓展 交付运行
        :param task_context:
        :return:
        """

        # 获取到爬虫的爬取结果
        # spider_token=54c82f27c0d74930a3a60517df1be0bc
        spider_result = self.spider_service.get_spider_result(task_context['spider_token'])
        print("!!!!!!!! spider_result: ", spider_result)

        # callback = 'http://{}/api/keyword-expansion/expand_keywords?task_token={}'.format(
        #     settings['expand_address'], task_context.token
        # )
        # expand_options = {}
        # # 发起关键词分析任务
        # expand_task = self.expand_service.submit_expand_task(spider_result=spider_result,
        #                                                      expand_options=expand_options,
        #                                                      callback=callback)
        #
        # task_context['expand_token'] = expand_task['analyze_token']
        # task_context['callback'] = expand_task['callback']
        #
        # self.task_context_service.suspend(task_context)

    def recover_after_expand_service_callback(self, task_token):
        task_context = self.task_context_service.awake(task_token)
        # TODO: 异步运行人工研判任务 manual_judge

    def manual_judge(self, task_context):
        """
        获取关键词拓展的结果，将 人工研判 的任务交付运行
        :param task_context:
        :return:
        """

        # 获取关键词拓展的结果
        expand_result = self.expand_service.get_expand_result(task_context['expand_token'])

        callback = 'http://{}/api/keyword-expansion/manual-judge?task_token={}'.format(
            settings['judge_address'], task_context.token
        )
        judge_options = {}
        # 提交分析任务并发起人工研判的通知
        judge_task = self.judge_service.submit_judge_task(expand_result=expand_result,
                                                          judge_options=judge_options,
                                                          callback=callback)
        task_context['judge_token'] = judge_task['judge_token']
        task_context['callback'] = judge_task['callback']

        self.task_context_service.susped(task_context)

    def recover_after_manual_judge_service_callback(self, task_token, manual_judge_result):
        """

        :param task_token:
        :param manual_judge_result: 从callback中获取的结果
        :return:
        """
        task_context = self.task_context_service.awake(task_token)
        # 存储人工研判结果
        self.judge_servic.save_judge_results(manual_judge_result)
        # 分析研判结果
        self.analyze_result(task_context)

    def analyze_result(self, task_context) -> list:
        """

        :param task_context:
        :return: 返回分析后的关键词列表 [{'word':--, 'key': ---, }]
        """
        pass

if __name__ == '__main__':

    KeywordExpansionModelService.start_keyword_expansion("hello")



