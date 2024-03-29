import os
import json
import urllib3
import requests
from time import sleep
from interfaceTest import getpathInfo

path = getpathInfo.get_Path()
xlsPath = os.path.join(path, 'result')


def test_report():

    lists = os.listdir(xlsPath)
    lists.sort(key=lambda fn: os.path.getmtime(xlsPath + "/" + fn))
    file_new = os.path.join(xlsPath, lists[-1])
    cs = os.path.basename(file_new)
    return cs


def new_report():

    sleep(10)
    hook_token = "https://oapi.dingtalk.com/robot/send?access_token" \
                 "=fd6ed0a8d8b8fe335dea97ac3b850c73c26363251948463c45b182bf9ca99eb1 "
    headers = {'content-type': 'application/json'}

    date = {

        "msgtype": "link",
        "link": {
            "text": "This is test report",
            "title": u"测试报告",
            "picUrl": "",
            "messageUrl": r"http://jks.aixiangdao.cn:83/" + test_report()
        }
    }

    urllib3.disable_warnings()
    r = requests.post(hook_token, headers=headers, data=json.dumps(date))
    r.encoding = 'utf-8'
