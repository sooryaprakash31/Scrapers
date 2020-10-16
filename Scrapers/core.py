from spiders.NDTVSpider import NDTVSpider


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(NDTVSpider)
process.start()