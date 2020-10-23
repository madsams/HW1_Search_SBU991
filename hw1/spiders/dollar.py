# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from hw1.items import DollarItem


def get_nested_text(resp, selector):
    text = ''
    for s in resp.css(selector).extract():
        text += my_strip(s)
    return text


def my_strip(s):
    if s is not None:
        return s.strip().replace(r'[\t\n]', '')
    else:
        return ""


class DollarSpider(scrapy.Spider):
    name = 'dollar'
    allowed_domains = ['donya-e-eqtesad.com']
    start_urls = [
        'https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1' + '/?page=%s' % page
        for page in range(1, 76)]
    BASE_URL = 'https://donya-e-eqtesad.com/'

    def parse(self, response, **kwargs):
        for service in response.css('li.service-special div.service-news-list'):
            link = service.css('h2.title a::attr(href)').get()
            if link:
                yield Request(
                    url=self.BASE_URL + link,
                    callback=self.parse_page2,
                    meta={'dont_redirect': True,
                          'handle_httpstatus_list': [302]
                          })

    def parse_page2(self, response):
        item = DollarItem()
        item['title'] = my_strip(response.css('h1.title::text').get())
        item['summery'] = get_nested_text(response, 'div.lead::text')
        item['content'] = response.css('#echo-detail div').get()
        item['date'] = response.css('time.news-time::attr(datetime)').extract()
        item['tags'] = response.css('a.tags-detail::attr(title)').extract()
        item['short_links'] = response.css('#short-l-copy::attr(value)').get()
        item['image_urls'] = response.css('.article-body img::attr(src)').extract()

        yield item
