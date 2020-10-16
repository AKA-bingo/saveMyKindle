# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SavemykindleItem(scrapy.Item):
    # define the fields for your item here like:
    chapterName = scrapy.Field()
    chapterUrl = scrapy.Field()
    chapterContent = scrapy.Field()
    pass
