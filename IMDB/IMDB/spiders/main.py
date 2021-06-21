import scrapy

class SctrQuotes(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']


    def parse(self, response):
        for i in response.css('.titleColumn a'):
            movieName = i.css('::text').get()
            url = i.css('::attr(href)').get()
            dic = {
                'movie': movieName,
            }
            yield response.follow(url, callback=self.parseInfo, meta=dic)




    def parseInfo(self, response):
            print('\n\n\n\n')
            movieName = response.meta['movie']
            duration = response.css('.subtext time::text').get().strip()
            genre = ', '.join(response.css('.subtext a:not(:last-child)::text').getall())

            # print(movieName, duration, genre)

            yield {
                'Movie Name': movieName,
                'Duration': duration,
                'Genre': genre
            }




