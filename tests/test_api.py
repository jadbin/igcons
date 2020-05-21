import requests
from conf import igcons
import json

# from guniflask.context import service
# from guniflask.config import settings

base_url = ""
server_address = igcons.server_address
headers = {'Content-Type': 'application/json'}


def test_trigger():
    """
    相当于对整个流程的测试
    :return:
    """
    url = 'http://{}/api/trigger'.format(server_address)
    data = {
        "keyword": "ttt",
        "spider_name": "baidu"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200

def test_spider_callback():
    """
    对数据获取执行后部分的测试
    :return:
    """

    task_token = '01ebfa2c-4d54-42ca-a500-e5066f368fc8'
    callback_url = 'http://{}/api/keyword-expansion/spider-service-callback?task_token={}'.format(
            server_address, task_token)
    data = {}
    response = requests.post(callback_url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200


# def test_expand_callback():
#     """
#     对关键词拓展后内容的测试
#     :return:
#     """
#
#     task_token = '3a10dcaa-4da9-417f-b0c2-5169f2a91f71'
#     callback_url = 'http://{}/api/keyword-expansion/expansion-callback?task_token={}'.format(
#         server_address, task_token)
#     data = {}
#     response = requests.post(callback_url, data=json.dumps(data), headers=headers)
#     assert response.status_code == 200
#
#
# def test_judge_callback():
#
#     url = ""
#     data
#
#
# def test_receive_judge_results():
#
#     url = ""
