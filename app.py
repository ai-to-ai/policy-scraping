from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.http import FormRequest
import re
from itemadapter import ItemAdapter

import schedule
import time

import openpyxl

# class CustomExporter(XlsxItemExporter):
#     def __init__(self, file, **kwargs):
#         super().__init__(file, include_header_row=False, **kwargs)

class PolicyScrapy(scrapy.Spider):
	name="Franchise"
	base_url = "https://www.franchiseball.com"

	custom_settings={
		# "ITEM_PIPELINES": {
		# 	'__main__.XLSXPipeline': 100
		# 	},
		"CONCURRENT_REQUESTS":32
	}

	url = "https://www.pfizer.com/Privacy#:~:text=We%20collect%20information%20about%20you,with%20your%20inquiries%20and%20purchases"

	def start_requests(self):
		yield scrapy.Request(url=self.url,callback=self.parse)

	def parse(self, response):
		# print(response.text)
		headers = response.xpath('//*[@class="accordion-list__title"]/text()').getall()
		contents = response.xpath(normalize-space('//*[@class="accordion-list__content"]')).get()
		print(headers)
		print(contents)


def start_crawl():
	print("Start Crawling...")
	configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
	runner = CrawlerRunner()
	d = runner.crawl(PolicyScrapy)
	d.addBoth(lambda _: reactor.stop())
	reactor.run()

start_crawl()
