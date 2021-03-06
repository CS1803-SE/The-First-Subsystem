import scrapy as scrapy

from ..items import *
from ..str_filter import *

class Museum38(scrapy.Spider):
    name = "Museum38"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%A4%A7%E8%BF%9E%E5%8D%9A%E7%89%A9%E9%A6%86/4532538?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 38
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = "辽宁省大连市沙河口区会展路10号"
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[53])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["openingTime"] = StrFilter.filter(item["openingTime"])
        item["consultationTelephone"] = None
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = StrFilter.filter(item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "121.5923"
        item["latitude"] = "38.8937"
        print(item)
        yield item
