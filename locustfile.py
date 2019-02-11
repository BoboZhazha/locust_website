#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-08 16:27
# @Author  : bobozhazha
# @File    : locustfile.py
# @Remark:

from locust import HttpLocust, TaskSet, task
from config import *
import random
from locust_log import *


class UserBehavior(TaskSet):

    @task
    def baidu_random(self):
        # 这个框架一个url,就要对应1个方法, 那我只能这样动态构建任务了
        url = random.choice(self.locust.url_list)
        log_info("当前测试的url是 : " + url)
        self.client.get(url, name=url)


class BaiduUser(HttpLocust):
    task_set = UserBehavior
    host = TARGET_URL
    url_list = []
    try:
        with open(URL_FILE, "r") as f:
            res = f.read()
            url_list = res.splitlines()
    except Exception as e:
        log_error("读取url_list失败,请检查路径是否正确")
        raise e
    min_wait = 1000
    max_wait = 2000


