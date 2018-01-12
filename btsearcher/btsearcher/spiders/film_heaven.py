# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector


class FilmHeavenSpider(scrapy.spiders.Spider):
    name = "film_heaven"
    start_urls =[
        "http://www.dytt8.net/"
    ]
    domain = "http://www.dytt8.net/"
    rules = [

    ]

    def parse(self,response):
        req = response.url
        body = response.body
        u_body = response.body_as_unicode()
        print body

