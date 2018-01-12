# -*- coding: utf-8 -*-
from __future__ import print_function, division
import re
import urllib, urllib2
import sys
from web_data import dianying_taobao,xinna

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error argvs")
        print("python server.py website search_key")
        exit(1)
    website = sys.argv[0]
    search = sys.argv[1]
    if website == "dianyingtaobao":
        reader = dianying_taobao.TaoBaoDianYing(search)
        reader.get_result()
    elif website == "xinna":
        reader = xinna.XinNa(search)
        reader.get_result()

