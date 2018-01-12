# -*- coding :utf-8 -*-
from __future__ import print_function, division
import urllib, urllib2
import scrapy

class XinNa:
    def get_result(self):
        print("finish Xinna")
        response = urllib2.urlopen(url=self.url)
        print(response.read())

    def __init__(self, target):
        # self.url = "https://dianying.taobao.com/"
        self.url = "http://mail.sina.com.cn/?from=mail"
        self.target = target


def __init__():
    pass