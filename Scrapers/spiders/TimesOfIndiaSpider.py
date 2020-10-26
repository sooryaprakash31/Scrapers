import scrapy

class TimesOfIndiaSpider(scrapy.Spider):

    name = "timesofindia"
    start_urls = ["https://timesofindia.indiatimes.com/briefs"]
    headlines = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_callback = kwargs.get('args').get('callback')
    
    #scrapes the required data from the response
    def parse(self, response):
        
        all_headlines = response.css('div.brief_box')
        for i in range(10):
            headline_text = all_headlines[i].css('h2 a::text').extract_first()
            headline_link = "https://timesofindia.indiatimes.com" + str(all_headlines[i].css('h2 a::attr(href)').extract_first())
            description = all_headlines[i].css('p a::text').extract_first()
            
            self.headlines[i] = {'text':headline_text, 'link': headline_link, 'desc': description}

    #execuctes when the spider finished scraping
    def close(self, spider, reason):
        self.output_callback(self.headlines,"TimesofIndia")
