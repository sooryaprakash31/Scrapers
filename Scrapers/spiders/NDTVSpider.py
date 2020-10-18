import scrapy

class NDTVSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = ["https://www.ndtv.com/top-stories"]

    def parse(self,response):

        all_headlines = response.css('div.new_storylising_contentwrap')
        for i in range(10):
            headline_text = all_headlines[i].css('h2.nstory_header a::attr(title)').extract_first()
            headline_link = all_headlines[i].css('h2.nstory_header a::attr(href)').extract_first()
            description = all_headlines[i].css('div.nstory_intro::text').extract_first()
            yield {
                'text': headline_text,
                'link': headline_link,
                'desc': description
            }