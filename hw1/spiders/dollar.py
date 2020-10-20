# -*- coding: utf-8 -*-
import scrapy


def get_nested_text(resp, selector):
    text = ''
    for s in resp.css(selector).extract():
        text += s.strip().replace(r'[\t\n]', '')
    return text


class DollarSpider(scrapy.Spider):
    name = 'dollar'
    allowed_domains = ['donya-e-eqtesad.com']
    start_urls = ['https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1']

    def parse(self, response, **kwargs):
        for service in response.css('li.service-special div.service-news-list'):
            title = service.css('h2.title a::attr(title)').get()
            yield {
                'title': title,
                'lead': get_nested_text(service, 'div.lead::text')
            }
