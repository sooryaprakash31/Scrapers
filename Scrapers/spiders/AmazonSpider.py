import scrapy

class AmazonSpider(scrapy.Spider):

    name = "amazon"
    start_urls = ["https://www.amazon.in/s?k="]
    products = {}


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_callback = kwargs.get('args').get('callback')
        self.product = kwargs.get('args').get('product')
        self.start_urls[0] = self.start_urls[0] + self.product

    def parse(self,respose):

        all_products_names = respose.css('.a-color-base.a-text-normal::text').extract()
        all_products_links = respose.css('.a-link-normal.a-text-normal::attr(href)').extract()
        all_products_prices = respose.css('.a-price-whole::text').extract()

        for i in range(5):
            product_name = all_products_names[i]
            product_price = all_products_prices[i]
            product_link = "https://www.amazon.in" + str(all_products_links[i])

            self.products[i] = {
                "name": product_name,
                "price":product_price,
                "link": product_link
            }

    def close(self, spider, reason):
        self.output_callback(self.products)