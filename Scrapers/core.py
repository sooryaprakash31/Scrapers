from spiders.NDTVSpider import NDTVSpider
from spiders.TimesOfIndiaSpider import TimesOfIndiaSpider
from spiders.AmazonSpider import AmazonSpider
from spiders.FlipkartSpider import FlipkartSpider

from scrapy.crawler import CrawlerProcess

import sys

# def start_crawlers(product):
#     process = CrawlerProcess()
#     process.crawl(NDTVSpider)
#     process.crawl(TimesOfIndiaSpider)
#     process.crawl(AmazonSpider,product=arg)
#     process.crawl(FlipkartSpider,product=arg)
#     process.start()

class StartCrawler:
    def __init__(self):
        self.output = None
        self.process = CrawlerProcess(settings={'LOG_ENABLED': False})

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

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    if arg is None:
        return_val = start_amazon(AmazonSpider, "mi a3")
        print("The result", return_val)

