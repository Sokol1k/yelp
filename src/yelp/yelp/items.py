# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class YelpItem(Item):
    name = Field()
    category = Field()
    address = Field()
    phone = Field()
    reviews = Field()
    rating = Field()
    image_urls = Field()
    images = Field()
    site = Field()
    workdays = Field()
