# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiyetaItem(scrapy.Item):
    name = scrapy.Field()
    about = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    district = scrapy.Field()
    occupation = scrapy.Field()
    education = scrapy.Field()
    url = scrapy.Field()
