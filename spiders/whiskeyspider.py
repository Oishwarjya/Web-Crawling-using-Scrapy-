import scrapy

class Whiskeyspider(scrapy.spider):
    name= 'whiskey'
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky']

    def parse(self,response):
        for product in response.css('div.product-item-info'):

            yield {
                'name':product.css('a.product-item-link::text').get(),
                'price':product.css('span.price::text').get().replace('£',''),
                'link':product.css('a.product-item-link').attrib['href']
            }