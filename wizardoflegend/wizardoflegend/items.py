# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Arcana(scrapy.Item):
    item_name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    element = scrapy.Field()
    type = scrapy.Field()
    damage = scrapy.Field()
    cooldown = scrapy.Field()
    knockback = scrapy.Field()
    duration = scrapy.Field()
    cost_gems = scrapy.Field()
    cost_coins = scrapy.Field()
    pool = scrapy.Field()
    image_urls = scrapy.Field()

class Relic(scrapy.Item):
    item_name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    cost_gems = scrapy.Field()
    cost_coins = scrapy.Field()
    pool = scrapy.Field()
    image_urls = scrapy.Field()