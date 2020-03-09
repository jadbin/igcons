# coding=utf-8

import uuid

from guniflask.context import service


class TaskContext:
    def __init__(self):
        self._token = uuid.uuid4()
        self._attributes = {}

    @property
    def token(self):
        return self._token

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
        pass

    def awake(self, task_token: str) -> TaskContext:
        """
        根据task token唤醒任务
        :param task_token: task token
        :return:
        """
        pass
