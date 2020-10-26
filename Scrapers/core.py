from spiders.NDTVSpider import NDTVSpider
from spiders.TimesOfIndiaSpider import TimesOfIndiaSpider
from spiders.AmazonSpider import AmazonSpider
from spiders.FlipkartSpider import FlipkartSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


import sys
import time

class StartCrawler:
    def __init__(self):
        # self.runner = CrawlerRunner()
        self.output = None
        self.process = CrawlerProcess(settings={LOG_ENABLED:False})

    def yield_output(self, data):
        self.output = data

    def crawl(self, cls, product=None):
        if product is not None:
            # d=self.runner.crawl(cls, args={'callback': self.yield_output, 'product':product})
            self.process.crawl(cls, args={'callback': self.yield_output, 'product':product})
        else:
            # d=self.runner.crawl(cls, args={'callback': self.yield_output})
            self.process.crawl(cls, args={'callback': self.yield_output})
        # d.addBoth(lambda _: reactor.stop())
        # reactor.run()
        # self.process.start()
        time.sleep(0.5)

def start_ndtv(cls):
    ndtv_crawler = StartCrawler()
    ndtv_crawler.crawl(cls)
    return ndtv_crawler.output

def start_timesofindia(cls):
    times_crawler = StartCrawler()
    times_crawler.crawl(cls)
    return times_crawler.output

def start_amazon(cls, product):
    amazon_crawler = StartCrawler()
    amazon_crawler.crawl(cls, product)
    return amazon_crawler.output

def start_flipkart(cls,product):
    flipkart_crawler = StartCrawler()
    flipkart_crawler.crawl(cls,product)
    return flipkart_crawler.output

class Controller:

    def __init__(self):
        self.output = {}
        self.runner = CrawlerProcess()

    def start_crawler(self,runner, spider, product=None):
        if product is not None:
            self.runner.crawl(spider, args={'callback': self.yield_output,'product':product})
        else:
            self.runner.crawl(spider, args={'callback': self.yield_output})

    def yield_output(self,data,spider_name):
        self.output[spider_name] = data

    def controller(self,keyword,product=None):

        if keyword == 'headlines':    
            self.start_crawler(self.runner,NDTVSpider)
            self.start_crawler(self.runner,TimesOfIndiaSpider)
        
        elif keyword == 'product':
            self.start_crawler(self.runner,AmazonSpider,product)
            self.start_crawler(self.runner,FlipkartSpider,product)

        self.runner.start()

        return self.output


control = Controller()

control.controller('headlines')



    

# def controller(keyword,product=None):

#     runner = CrawlerProcess()

#     if keyword == 'headlines':    
#         start_crawler(runner,NDTVSpider)
#         start_crawler(runner,TimesOfIndiaSpider)
    
#     elif keyword == 'product':
#         start_crawler(runner,AmazonSpider,product)
#         start_crawler(runner,FlipkartSpider,product)

#     runner.start()

# runner = CrawlerProcess()
# start_crawler(runner,NDTVSpider)
# start_crawler(runner,TimesOfIndiaSpider)
# runner.start()


# # print(start_ndtv(NDTVSpider))
# # print(start_timesofindia(TimesOfIndiaSpider))
# # print(start_amazon(AmazonSpider,"mi a3"))
# # print(start_flipkart(FlipkartSpider,"mi a3"))



