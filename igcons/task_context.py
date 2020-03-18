# coding=utf-8

import uuid
import os
import pickle

from guniflask.context import service
from guniflask.config import settings

class TaskContext:
    def __init__(self):
        self._token = uuid.uuid4()
        self._attributes = {}

    @property
    def token(self):
        return self._token

    @property
    def attributes(self):
        return self._attributes

    def __getitem__(self, key):
        return self._attributes.get(key)

    def __setitem__(self, key, value):
        self._attributes[key] = value

    def __delitem__(self, key):
        if key in self._attributes:
            self._attributes.pop(key)


@service
class TaskContextService:
    def __init__(self):
        pass

    def suspend(self, task_context: TaskContext):
        """
        挂起任务
        :param task_context: task上下文
        """
        task_token = str(task_context.token)
        with open(os.path.join(settings['task_context_dir'], task_token) + ".pkl", "wb") as f:
            pickle.dump(task_context, f)


    def awake(self, task_token: str) -> TaskContext:
        """
        根据task token唤醒任务
        :param task_token: task token
        :return:
        """
        with open(os.path.join(settings['task_context_dir'], str(task_token)) + ".pkl", "rb") as f:
            return pickle.load(f)
