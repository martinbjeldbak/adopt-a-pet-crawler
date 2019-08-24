# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdoptapetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Pet(scrapy.Item):
    sex = scrapy.Field()
    is_desexed = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    updated_at = scrapy.Field()
    date_of_birth = scrapy.Field()
    description = scrapy.Field()
    adoption_cost = scrapy.Field()
