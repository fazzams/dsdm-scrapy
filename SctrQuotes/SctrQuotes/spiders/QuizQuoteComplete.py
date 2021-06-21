import scrapy

class SctrQuotes(scrapy.Spider):
    name = 'quiz'
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        for div in response.css('.quote'):
            tags = div.css('.tag::text').getall()
            tags = ', '.join(tags)
            yield {
                'Quote': div.css('.text::text').get(),
                'Author': div.css('.author::text').get(),
                'Tag': tags
            }

        nextPageUrl = response.css('li.next a::attr(href)').get()
        print(nextPageUrl)

        if nextPageUrl:
            yield response.follow(nextPageUrl, callback=self.parse)
        else:
            print('\n\n\n\n\n This is the last page')



