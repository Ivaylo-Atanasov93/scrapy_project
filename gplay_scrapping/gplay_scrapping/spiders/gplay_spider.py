import urllib.parse

import scrapy
from ..items import GplayScrappingItem


class GplayProductsSpider(scrapy.Spider):
    name = 'gplay_spider'
    start_urls = [
        'https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D0%BF%D0%B5%D1%80%D0%B8%D1%84%D0%B5%D1%80%D0%B8%D1%8F',
        'https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D1%85%D0%B0%D1%80%D0%B4%D1%83%D0%B5%D1%80',
    ]

    def parse(self, response, **kwargs):
        subcategories = []
        for link in response.css('div.categories-grid-item a::attr(href)').getall():
            subcategories.append(self.clean_link(link))

        for link in subcategories:
            yield response.follow(link.decode('utf8'), callback=self.parse_subcategories)

    def parse_subcategories(self, response):
        product_links = []
        for link in response.css('div.product-item a::attr(href)').getall():
            product_links.append(self.clean_link(link))

        next_page = response.css('li.page-item a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_subcategories)

        for link in product_links:
            yield response.follow(link.decode('utf8'), callback=self.parse_product)

    def parse_product(self, response):
        items = GplayScrappingItem()
        price = float(response.xpath("//div[contains(@class, 'product-price-controls')]//price/@*").get())
        status = response.css('nobr::text').get()

        if price < 200 and status == 'наличен':
            title = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/h1/text()').get().strip()
            subtitle = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/h2/text()').get().strip()
            product_number = response.xpath(
                '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/strong/text()').get().strip()
            category = response.xpath('//*[@id="content"]/div[1]/div[1]/a[2]/text()').get().strip()
            subcategory = response.xpath('//*[@id="content"]/div[1]/div[1]/a[3]/text()').get().strip()

            items['category'] = category
            items['subcategory'] = subcategory
            items['title'] = title
            items['subtitle'] = subtitle
            items['product_number'] = product_number
            items['price'] = price
            yield items

    def clean_link(self, link):
        cleaned_link = urllib.parse.urlparse(link)
        cleaned_link = cleaned_link._replace(path=urllib.parse.quote(cleaned_link.path.encode('utf8')))
        encoded_url = cleaned_link.geturl().encode('ascii')
        return encoded_url
