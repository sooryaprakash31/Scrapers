import scrapy

class NDTVSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = ["https://www.ndtv.com/top-stories"]
    headlines = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_callback = kwargs.get('args').get('callback')

    #scrapes the required data from the response    
    def parse(self,response):

        all_headlines = response.css('div.new_storylising_contentwrap')

        for i in range(10):
            headline_text = all_headlines[i].css('h2.nstory_header a::attr(title)').extract_first()
            headline_link = all_headlines[i].css('h2.nstory_header a::attr(href)').extract_first()
            description = all_headlines[i].css('div.nstory_intro::text').extract_first()

            self.headlines[i] = {'text':headline_text, 'link': headline_link, 'desc': description}

    
    #execuctes when the spider finished scraping
    def close(self, spider, reason):
        self.output_callback(self.headlines,"NDTV")
