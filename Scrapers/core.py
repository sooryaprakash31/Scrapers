from spiders.NDTVSpider import NDTVSpider
from spiders.TimesOfIndiaSpider import TimesOfIndiaSpider
from spiders.AmazonSpider import AmazonSpider
from spiders.FlipkartSpider import FlipkartSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys
import time

class StartCrawler:
    def __init__(self):
        self.output = None
        self.process = CrawlerProcess()

    def yield_output(self, data):
        self.output = data

    def crawl(self, cls, product=None):
        if product is not None:
            self.process.crawl(cls, args={'callback': self.yield_output, 'product':product})
        else:
            self.process.crawl(cls, args={'callback': self.yield_output})
        self.process.start()

def start_ndtv(cls):
    crawler = StartCrawler()
    crawler.crawl(cls)
    return crawler.output

def start_timesofindia(cls):
    crawler = StartCrawler()
    crawler.crawl(cls)
    return crawler.output

def start_amazon(cls, product):
    crawler = StartCrawler()
    crawler.crawl(cls, product)
    return crawler.output

def start_flipkart(cls,product):
    crawler = StartCrawler()
    crawler.crawl(cls,product)
    return crawler.output


print(start_ndtv(NDTVSpider))
print(start_timesofindia(TimesOfIndiaSpider))
print(start_amazon(AmazonSpider,"mi a3"))
print(start_flipkart(FlipkartSpider,"mi a3"))



