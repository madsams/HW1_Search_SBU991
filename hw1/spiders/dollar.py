# -*- coding: utf-8 -*-
import scrapy


class DollarSpider(scrapy.Spider):
    name = 'dollar'
    allowed_domains = ['donya-e-eqtesad.com']
    start_urls = ['https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1']

    def parse(self, response, **kwargs):
        service = response.css('service-special')
        yield {service}
