import scrapy

class TimesOfIndiaSpider(scrapy.Spider):

    name = "timesofindia"
    start_urls = ["https://timesofindia.indiatimes.com/briefs"]

    def parse(self, response):
        
        all_headlines = response.css('div.brief_box')
        for i in range(10):
            headline_text = all_headlines[i].css('h2 a::text').extract_first()
            headline_link = "https://timesofindia.indiatimes.com" + str(all_headlines[i].css('h2 a::attr(href)').extract_first())
            description = all_headlines[i].css('p a::text').extract_first()
            yield {
                'text': headline_text,
                'link': headline_link,
                'desc': description
            }
            return {
                'text': headline_text,
                'link': headline_link,
                'desc': description
            }
