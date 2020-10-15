import scrapy

class NDTVSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = ["https://www.ndtv.com/top-stories"]

    def parse(self,response):

        all_headers = response.css('h2.nstory_header')
        all_headers_links = response.css('h2.nstory_header a::attr(href)').extract()
        all_header_text = response.css('h2.nstory_header a::attr(title)').extract()
        
        for header in all_headers:
            header_text = header.css('a::attr(title)').extract()
            header_link = header.css('a::attr(href)').extract()
            yield {
                'headers': text
            }