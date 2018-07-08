# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeautyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	col = 'beauty_im'
	id = scrapy.Field()
	url = scrapy.Field()
	title = scrapy.Field()
	thumb = scrapy.Field()
	