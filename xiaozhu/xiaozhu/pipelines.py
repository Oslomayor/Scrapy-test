# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaozhuPipeline(object):
    def process_item(self, item, spider):
        fp = open('E:\AllPrj\PyCharmPrj\py-crawler\Scrapy 爬虫框架测试\\xiaozhu\\results.txt', 'a+', encoding='utf-8')
        fp.write(str(item['title'])+'\n')
        fp.write(str(item['address'])+'\n')
        fp.write(str(item['price'])+'\n')
        fp.write(str(item['lease_type'])+'\n')
        fp.write(str(item['person'])+'\n')
        fp.write(str(item['bed'])+'\n')
        fp.close()
        return item
