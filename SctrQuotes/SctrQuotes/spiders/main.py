import scrapy

class SctrQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('RESPONSE FROM SERVER: ', response.url)
        print('STATUS FROM SERVER: ', response.status)
        print('HEADER FROM SERVER: ', response.headers)

        print("BODY FROM SERVER: ", type(response.body.decode('utf-8')))

        print('VALUE FROM HEADER: ', type(response.headers.get('Server').decode('utf-8')))
        print('VALUE FROM HEADER: ', type(response.headers.get('Content-Type').decode('utf-8')))
        print("\n\n\n\n--------------------")

        pass