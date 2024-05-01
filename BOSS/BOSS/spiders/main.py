import scrapy
from scrapy import Request

class SctrQuotes(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/home']

    def parse(self, response):
        # a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a
        cssSel = 'a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a::attr(href)'
        for url in response.css(cssSel).getall():
            yield Request(url, callback=self.parseProducts)

    def parseProducts(self, response):
        cssSel2 = '.product-tile-default__gallery a::attr(href)'
        for prodUrl in response.css(cssSel2).getall():
            yield response.follow(prodUrl, callback=self.parseProduct)

        nextPageCss = '.button.button--pagingbar.pagingbar__next.font__nav-link::attr(href)'
        nextPageUrl = response.css(nextPageCss).get()

        if nextPageUrl:
            yield Request(nextPageUrl, callback=self.parseProduct)


    def parseProduct(self, response):
        productName = response.css('.pdp-stage__header-title::text').get().strip()
        colour = response.css('.color-selector__text::text').getall()
        colour = ', '.join(colour)
        
        datasrc = response.css('.pdp-images__adaptive-picture img::attr(data-src)').getall()
        picUrls = ', '.join(datasrc)
        picUrls = picUrls.replace('&wid={width}&qlt={quality}', '')

        careIns = response.css('.care-info > .care-info__text::text').getall()
        careIns = ', '.join(careIns)

        yield {
            'Product': productName,
            'Colour': colour,
            'Picture': picUrls,
            'Care Instructions': careIns
        }

        # datasrc = response.css('.pdp-images__adaptive-picture img::attr(data-src)').getall()
        # datasrc2 = []
        # for i in datasrc:
        #   i2 = i.replace('&wid={width}&qlt={quality}', '')
        #   datasrc2.append(i2)
        # picUrls = ', '.join(datasrc)
        # picUrls = picUrls.replace('&wid={width}&qlt={quality}', '')
        # Test




