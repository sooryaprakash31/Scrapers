from spiders.NDTVSpider import NDTVSpider
from spiders.TimesOfIndiaSpider import TimesOfIndiaSpider
from spiders.AmazonSpider import AmazonSpider
from spiders.FlipkartSpider import FlipkartSpider

from scrapy.crawler import CrawlerProcess


import sys
import time

class Controller:

    def __init__(self):
        self.output = {}
        self.runner = CrawlerProcess(settings={'LOG_ENABLED': False})

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

#returns a dict with spider_name as key. 
control.controller('headlines')
