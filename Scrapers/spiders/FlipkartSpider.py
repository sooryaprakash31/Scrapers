import scrapy

class FlipkartSpider(scrapy.Spider):
    
    name = "flipkart"
    start_urls = ["https://www.flipkart.com/search?q="]
    products = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_callback = kwargs.get('args').get('callback')
        self.product = kwargs.get('args').get('product')
        self.start_urls[0] = self.start_urls[0] + self.product
    
    def parse(self, response):

        all_products_names = response.css('._3wU53n::text').extract()
        all_products_prices = response.css('._2rQ-NK::text').extract()
        all_products_links = response.css('._31qSD5::attr(href)').extract()

        for i in range(10):

            product_name = all_products_names[i]
            product_price = all_products_prices[i]
            product_link = "https://www.flipkart.com" +all_products_links[i]

            self.products[i] = {
                "name": product_name,
                "price":product_price,
                "link": product_link
            }
    
    def close(self, spider, reason):
        self.output_callback(self.products)