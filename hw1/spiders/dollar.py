# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


def get_nested_text(resp, selector):
    text = ''
    for s in resp.css(selector).extract():
        text += s.strip().replace(r'[\t\n]', '')
    return text


class DollarItem(scrapy.Item):
    title = scrapy.Field()
    lead = scrapy.Field()
    body = scrapy.Field()


class DollarSpider(scrapy.Spider):
    name = 'dollar'
    allowed_domains = ['donya-e-eqtesad.com']
    start_urls = ['https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1']
    BASE_URL = 'https://donya-e-eqtesad.com/'

    def parse(self, response, **kwargs):
        for service in response.css('li.service-special div.service-news-list'):
            item = DollarItem()
            item['title'] = service.css('h2.title a::attr(title)').get()
            item['lead'] = get_nested_text(service, 'div.lead::text')
            link = service.css('h2.title a::attr(href)').get()
            if link:
                yield Request(url=self.BASE_URL + link, callback=self.parse_page2, meta={'item': item})

    def parse_page2(self, response):
        item = response.meta['item']
        item['body'] = response.css('body').get()
        yield item
