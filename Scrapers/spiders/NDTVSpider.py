import scrapy

class NDTVSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = ["https://www.ndtv.com/top-stories"]

    def parse(self,response):

        all_headlines = response.css('div.new_storylising_contentwrap')
        for i in range(10):
            header_text = all_headlines[i].css('h2.nstory_header a::attr(title)').extract()
            header_link = all_headlines[i].css('h2.nstory_header a::attr(href)').extract()
            description = all_headlines[i].css('div.nstory_intro::text').extract()
            yield {
                'text': header_text,
                'link': header_link,
            }