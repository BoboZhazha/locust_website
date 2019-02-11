#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-09 16:27
# @Author  : bobozhazha
# @File    : locust_log.py
# @Remark: 日志模块


import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("locust.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)


def log_info(msg):
    logger.info(msg)


def log_error(msg):
    logger.error(msg)




