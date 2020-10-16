from spiders.NDTVSpider import NDTVSpider
from spiders.HinduSpider import HinduSpider

from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(NDTVSpider)
process.crawl(HinduSpider)
process.start()