# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
#https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttcrawlerSpider(scrapy.Spider):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Stock/M.1595557095.A.94D.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        pass
