import scrapy

class HinduSpider(scrapy.Spider):
    name = "hindu"
    start_urls = ["https://www.thehindu.com/latest-news/"]

    def parse(self,response):

        all_headlines = response.css('ul.latest-news a::text').extract()
        all_links = response.css('ul.latest-news a::attr(href)').extract()
        for i in range(10):
            headline_text = all_headlines[i]
            headline_link = all_links[i]
            
            yield {
                'text':headline_text,
                'link':headline_link
            }
            