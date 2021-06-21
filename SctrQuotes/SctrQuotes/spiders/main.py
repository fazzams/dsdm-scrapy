import scrapy

class SctrQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):

        for div in response.css('.quote'):
            quote = div.css('.text::text').get()
            author = div.css('.author::text').get()
            yield {
                'quote': quote.replace('“','').replace('”', ''),
                'author': author
            }

        nextPageUrl = response.css('li.next a::attr(href)').get()
        print(nextPageUrl)

        if nextPageUrl:
            yield response.follow(nextPageUrl, callback=self.parse)
        else:
            print('\n\n\n\n\n This is the last page')


        # print("\n\n--------------------")
        # for quote in response.css('.text::text').getall():
        #     yield {
        #         'quotes': quote
        #     }
        # print("\n\n--------------------")



        # print('RESPONSE FROM SERVER: ', response.url)
        # print('STATUS FROM SERVER: ', response.status)
        # print('HEADER FROM SERVER: ', response.headers)
        #
        # print("BODY FROM SERVER: ", type(response.body.decode('utf-8')))
        #
        # print('VALUE FROM HEADER: ', type(response.headers.get('Server').decode('utf-8')))
        # print('VALUE FROM HEADER: ', type(response.headers.get('Content-Type').decode('utf-8')))
        #
        # print(response.request)

        print("\n\n--------------------")

        pass