# -*- coding: utf-8 -*-
import scrapy


class DollarSpider(scrapy.Spider):
    name = 'dollar'
    allowed_domains = ['donya-e-eqtesad.com']
    start_urls = ['http://donya-e-eqtesad.com/']

    def parse(self, response):
        pass
