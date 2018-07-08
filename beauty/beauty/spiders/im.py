# -*- coding: utf-8 -*-
import scrapy


class ImSpider(scrapy.Spider):
    name = 'im'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def parse(self, response):
        pass
