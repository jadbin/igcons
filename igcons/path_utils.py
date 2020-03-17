# coding=utf-8

import os
from os.path import join, abspath
from functools import wraps

from guniflask.context import service
from guniflask.config import settings


def create_if_not_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        path = func(*args, **kwargs)
        if isinstance(path, str):
            os.makedirs(path, exist_ok=True)
        return path

    return wrapper


@service
class PathUtils:
    """
    返回业务常用路径
    """

    @property
    def home_dir(self):
        return settings['home']

    @property
    @create_if_not_exists
    def data_dir(self):
        return join(settings['home'], '.data')

    @property
    @create_if_not_exists
    def temp_dir(self):
        return join(settings['home'], '.temp')

    @create_if_not_exists
    def app_data_dir(self, app_name, *args):
        return join(self.data_dir, abspath(join('/', app_name, *args)))

    @create_if_not_exists
    def app_temp_dir(self, app_name, *args):
        return join(self.temp_dir, abspath(join('/', app_name, *args)))

    @property
    def spider_dir(self):
        return settings['spider_dir']

    @property
    def spider_result_dir(self):
        return join(self.spider_dir, ".spider_data/")

    @property
    def spider_result_file(self):
        return "result.json"
