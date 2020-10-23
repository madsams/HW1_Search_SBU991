# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DollarItem(scrapy.Item):
    title = scrapy.Field()
    summery = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    short_links = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
