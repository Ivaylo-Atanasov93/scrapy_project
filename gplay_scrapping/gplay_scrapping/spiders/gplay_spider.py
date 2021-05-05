import urllib.parse

import scrapy


class GplayProductsSpider(scrapy.Spider):
    name = 'gplay_spider'
    start_urls = [
        'https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D0%BF%D0%B5%D1%80%D0%B8%D1%84%D0%B5%D1%80%D0%B8%D1%8F',
        'https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D1%85%D0%B0%D1%80%D0%B4%D1%83%D0%B5%D1%80',
    ]

    def parse(self, response, **kwargs):
        subcategories = []
        for link in response.css('div.categories-grid-item a::attr(href)').getall():
            cleaned_link = urllib.parse.urlparse(link)
            cleaned_link = cleaned_link._replace(path=urllib.parse.quote(cleaned_link.path.encode('utf8')))
            encoded_url = cleaned_link.geturl().encode('ascii')
            subcategories.append(encoded_url)
        for link in subcategories:
            print(link)
            yield response.follow(link.decode('utf8'), callback=self.parse_subcategories)

    def parse_subcategories(self, response):
        product_links = []
        for link in response.css('div.product-item a::attr(href)').getall():
            cleaned_link = urllib.parse.urlparse(link)
            cleaned_link = cleaned_link._replace(path=urllib.parse.quote(cleaned_link.path.encode('utf8')))
            encoded_url = cleaned_link.geturl().encode('ascii')
            product_links.append(encoded_url)
        print(product_links)
        for link in product_links:
            yield response.follow(link.decode('utf8'), callback=self.parse_product)

    def parse_product(self, response):
        print(response.css('.float').css('::text').extract())
        # print(response.css('div.int::text').extract_first())
