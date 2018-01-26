# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from btsearcher.items import BtsearcherItem

class FilmHeavenSpider(scrapy.spiders.Spider):
    name = "film_heaven"
    start_urls =[
        "http://www.dytt8.net/html/gndy/dyzz/index.html"
    ]
    domain = "dytt8.net"
    base_url = "http://www.dytt8.net/html/gndy/dyzz/"
    url_sets = []
    result_dict = dict()

    def parse3(self,responce):
        item = BtsearcherItem()
        item["name"] = responce.meta["name"]
        item["addr"] = responce.xpath('//tbody//@href')[0].extract()
        yield item
    def parse2(self,response):
        results = response.xpath('//tr//td/b/a')
        for film in results:
            name = film.xpath('./text()')[0].extract().encode('utf-8')
            addr = "http://www.dytt8.net" + film.xpath('./@href')[0].extract()
            yield Request(addr, callback=self.parse3,meta={'name':name})
    def parse(self,response):
        req = response.url
        body = response.body
        u_body = response.body_as_unicode()
        if response.url in self.start_urls:
            tmp_urls = response.xpath('//div/td/select/option')
            for url in tmp_urls:
                relate_url = self.base_url + url.xpath('@value')[0].extract()
                if relate_url not in self.url_sets:
                    self.url_sets.append(relate_url)
                    yield Request(relate_url,callback=self.parse2)






