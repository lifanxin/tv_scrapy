# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IpProxiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 如果有新的字段添加进来，可以继承这个类再去定义新的
    ip = scrapy.Field()
    port = scrapy.Field()
    address = scrapy.Field()
    protocol = scrapy.Field()
    ttl = scrapy.Field()
