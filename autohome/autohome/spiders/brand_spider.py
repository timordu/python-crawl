# coding=utf-8

import scrapy
import time
from autohome.items import BrandItem


class BrandSpider(scrapy.Spider):
    name = "brand"
    allowed_domains = 'autohome.com.cn'
    url = 'https://www.autohome.com.cn/grade/carhtml/%s.html'

    start_urls = ['https://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]

    # 测试地址
    # start_urls = ['https://www.autohome.com.cn/grade/carhtml/A.html']

    def parse(self, response):
        print("===>", response.url)
        for brands in response.xpath('body/dl'):
            brand = BrandItem()
            brand['id'] = brands.xpath('@id')[0].extract()
            brand['name'] = brands.xpath('dt/div/a/text()')[0].extract()
            brand['logo'] = 'https:' + brands.xpath('dt/a/img/@src')[0].extract()
            brand['initial'] = response.url[42:43]
            brand['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            yield brand
