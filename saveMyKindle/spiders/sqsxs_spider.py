import scrapy

from saveMyKindle.items import SavemykindleItem

class SqsxsSpider(scrapy.Spider):
    name = "sqsxs"
    start_urls = [
        "https://www.sqsxs.com/book/x/xxx/"
   ]
    def parse(self, response):
        for sel in response.xpath('//dd'):
            item = SavemykindleItem()
            if len(sel.xpath('a/text()').extract()) == 0:
                continue
            item["chapterName"] = sel.xpath('a/text()').extract()[0]
            item["chapterUrl"] = "".join(self.start_urls + sel.xpath('a/@href').extract())
            yield scrapy.Request(item['chapterUrl'], meta={'item': item}, callback=self.content_parse)


    def content_parse(self, response):
        item = response.meta['item']
        item["chapterContent"] = "".join(response.xpath('//div[@id="content"]/text()').extract())
        return item
