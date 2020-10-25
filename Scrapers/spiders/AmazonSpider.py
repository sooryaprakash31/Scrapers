import scrapy

class AmazonSpider(scrapy.Spider):

    name = "amazon"
    start_urls = ["https://www.amazon.in/s?k="]

    def __init__(self, product):
        product = product.replace(" ","+")
        self.start_urls[0] = self.start_urls[0] + product

    def parse(self,respose):

        all_products_names = respose.css('.a-color-base.a-text-normal::text').extract()
        all_products_links = respose.css('.a-link-normal.a-text-normal::attr(href)').extract()
        all_products_prices = respose.css('.a-price-whole::text').extract()

        for i in range(5):
            product_name = all_products_names[i]
            product_price = all_products_prices[i]
            product_link = "https://www.amazon.in" + str(all_products_links[i])

            # yield {
            #     "product_name": product_name,
            #     "product_price":product_price,
            #     "product_link": product_link
            # }

            return {
                "product_name": product_name,
                "product_price":product_price,
                "product_link": product_link
            }

