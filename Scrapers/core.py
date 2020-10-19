from spiders.NDTVSpider import NDTVSpider
from spiders.TimesOfIndiaSpider import TimesOfIndiaSpider
from spiders.AmazonSpider import AmazonSpider

from scrapy.crawler import CrawlerProcess

import sys

def start_crawlers(product):
    process = CrawlerProcess()
    # process.crawl(NDTVSpider)
    # process.crawl(TimesOfIndiaSpider)
    process.crawl(AmazonSpider,product=arg)
    process.start()


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    if arg is not None:
        return_val = start_crawlers(product=arg)