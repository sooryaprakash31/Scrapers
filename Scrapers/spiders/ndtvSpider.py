import scrapy

class NDTVSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = ["https://www.ndtv.com/top-stories"]

    def parse(self,response):

        all_headlines = response.css('div.new_storylising_contentwrap')
        for header in all_headlines:
            header_text = header.css('h2.nstory_header a::attr(title)').extract()
            header_link = header.css('h2.nstory_header a::attr(href)').extract()
            description = header.css('div.nstory_intro::text').extract()
            yield {
                'text': header_text,
                'link': header_link,
                'desc': description
            }