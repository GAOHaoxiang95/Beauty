# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy import Spider, Request
import json
from beauty.items import BeautyItem
class ImSpider(scrapy.Spider):
	name = 'im'
	allowed_domains = ['images.so.com']
	start_urls = ['http://images.so.com/']

	def start_requests(self):
		data = {'ch':'beauty', 't1':'595', 'eid':'t01aa0205686cc0182e.jpg', 'listtype':'new'}
		base_url = 'http://images.so.com/zj?'
		
		for page in range(0, 1):
			data['sn'] = page*30
			parameters = urllib.parse.urlencode(data)
			url = base_url + parameters
			yield Request(url, self.parse)
			
	def parse(self, response):
		result = json.loads(response.text)
		
		for image in result.get('list'):
			item = BeautyItem()
			item['id'] = image.get('imageid')
			item['url'] = image.get('qhimg_url')
			item['title'] = image.get('group_title')
			item['thumb'] = image.get('qhimg_thumb_url')
			yield item
