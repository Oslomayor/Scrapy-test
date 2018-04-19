# Apr 19th, 2018, 2:16PM, @ dorm 602
# Scrapy 爬虫框架测试
# 爬取小猪短租网站的信息

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector 
from xiaozhu.items import XiaozhuItem

class xiaozhu(CrawlSpider):
	name = 'xiaozhu'
	start_urls = ['http://hz.xiaozhu.com/fangzi/28592402903.html']

	def parse(self, response):
		item = XiaozhuItem()
		selector = Selector(response)

		title = selector.xpath('//h4/em/text()')[0]
		address = selector.xpath('//p/span/text()').extract()[0].strip()
		price = selector.xpath('//*[@id="pricePart"]/div[1]/span/text()').extract()[0]
		lease_type = selector.xpath('//*[@id="introduce"]/li[1]/h6/text()').extract()[0]
		person = selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
		bed = selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]

		item['title'] = title
		item['address'] = address
		item['price'] = price 
		item['lease_type'] = lease_type 
		item['person'] = person 
		item['bed'] = bed 

		yield item 