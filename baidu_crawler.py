#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-09 16:26
# @Author  : bobozhazha
# @File    : baidu_crawler.py
# @Remark: 访问首页,获取链接

import requests
from bs4 import BeautifulSoup
from config import TARGET_URL, URL_FILE
from locust_log import *


# 获取网页html, dynamic_mode为True则获取渲染后的网页
def get_html(dynamic_mode=False, url=TARGET_URL):
    if dynamic_mode:
        from selenium import webdriver
        try:
            browser = webdriver.Chrome(executable_path="./chromedriver")
            browser.get(url)
            html_str = browser.page_source
            browser.close()
            return html_str
        except Exception as e:
            log_error("通过浏览器获得html出错,请检查驱动路径,版本是否匹配,url是否正确")
            browser.close()
            raise e
    else:
        resp = requests.get(url=url)
        resp.encoding = 'utf-8'
        return resp.text


# 解析所有a链接并且返回
def get_urls(html_str):
    soup = BeautifulSoup(html_str, "lxml")
    all_a = soup.find_all("a", href=True)
    all_href = [x['href'] for x in all_a]
    # 百度首页里有几个以//开头的飞网址,这里直接滤掉
    result = filter(lambda x: x.startswith("http"), all_href)
    return result


# 持久化,这里直接写txt
def write_url(urls):
    # 写模式,每次写新的
    with open(URL_FILE, "w") as f:
        for i in urls:
            f.write(i + "\n")


# 如果需要单独运行就这样,也可以在locustfile模块里BaiduUser类里调用
if __name__ == '__main__':
    # 使用动态模式,也可以置为False
    html = get_html(dynamic_mode=True)
    all_urls = get_urls(html)
    write_url(all_urls)
