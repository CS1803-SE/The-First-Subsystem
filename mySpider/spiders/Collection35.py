#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 17:14 
# @Author  : ana
# @File    : Collection35.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection35_supporting


class Collection35(scrapy.Spider):
    name = "Collection35"
    allowed_domains = ['918museum.org.cn']
    start_urls = Collection35_supporting.Collection35Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 35
            item["museumName"] = "“九·一八”历史博物馆"
            item['collectionName'] = li.xpath("./a/img/@alt").extract_first()
            item['collectionImageLink'] = 'http://www.918museum.org.cn' + str(li.xpath(
                "./a/img/@src").extract_first())
            url = "http://www.918museum.org.cn" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='frameContent']/p[2]").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
