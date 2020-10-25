import scrapy

class FlipkartSpider(scrapy.Spider):
    
    name = "flipkart"
    start_urls = ["https://www.flipkart.com/search?q="]

    def __init__(self, product):
        product = product.replace(" ","+")
        self.start_urls[0] = self.start_urls[0] + product
    def parse(self, response):

        all_products_names = response.css('._3wU53n::text').extract()
        all_products_prices = response.css('._2rQ-NK::text').extract()
        all_products_links = response.css('._31qSD5::attr(href)').extract()

        for i in range(10):

            product_name = all_products_names[i]
            product_price = all_products_prices[i]
            product_link = "https://www.flipkart.com" +all_products_links[i]
        
            # yield {
            #     "product_name":product_name,
            #     "product_price": product_price,
            #     "product_link": product_link
            # }

            return {
                "product_name": product_name,
                "product_price":product_price,
                "product_link": product_link
            }