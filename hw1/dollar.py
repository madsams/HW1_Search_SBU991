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
