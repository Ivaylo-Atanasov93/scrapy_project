# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GplayScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    category: [str] = scrapy.Field()
    subcategory: [str] = scrapy.Field()
    title: [str] = scrapy.Field()
    subtitle: [str] = scrapy.Field()
    product_number: [str] = scrapy.Field()
    price: [float] = scrapy.Field()
