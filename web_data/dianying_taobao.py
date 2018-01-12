# -*- coding :utf-8 -*-
from __future__ import print_function, division
import urllib, urllib2

class TaoBaoDianYing:
    def get_result(self):
        print("finish taobaodianying")
        response = urllib2.urlopen(url=self.url)
        print(response.read())

    def __init__(self, target):
        # self.url = "https://dianying.taobao.com/"
        self.url = "https://login.taobao.com/member/login.jhtml"
        self.target = target


def __init__():
    pass
