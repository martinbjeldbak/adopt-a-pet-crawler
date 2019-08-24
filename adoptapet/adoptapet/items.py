# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdoptapetItem(scrapy.Item):
    pass

class Pet(AdoptapetItem):
    id = scrapy.Field()
    api_id = scrapy.Field()
    url = scrapy.Field()
    sex = scrapy.Field()
    is_desexed = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    date_of_birth = scrapy.Field()
    description = scrapy.Field()
    adoption_cost = scrapy.Field()
    readable_age = scrapy.Field()
    name = scrapy.Field()
    had_behavior_evaluated = scrapy.Field()
    had_health_checked = scrapy.Field()
    is_vaccinated = scrapy.Field()
    is_wormed = scrapy.Field()
    is_special_needs_okay = scrapy.Field()
    is_long_term_resident = scrapy.Field()
    is_senior_pet = scrapy.Field()
    is_microchipped = scrapy.Field()
    is_active = scrapy.Field()
