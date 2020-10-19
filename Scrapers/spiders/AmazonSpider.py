import scrapy

class AmazonSpider(scrapy.Spider):

    name = "amazon"
    start_urls = ["https://www.amazon.in/s?k="]

    def __init__(self, product):
        product = product.replace(" ","+")
        AmazonSpider.start_urls = ["https://www.amazon.in/s?k="+product]

    def parse(self,respose):

        all_products_names = respose.css('.a-color-base.a-text-normal::text').extract()
        all_products_links = respose.css('.a-link-normal.a-text-normal::attr(href)').extract()
        for i in range(5):
            product_name = all_products_names[i]
            product_link = "https://www.amazon.in" + str(all_products_links[i])
            
            yield {
                "product_name": product_name,
                "product_link": product_link
            }

