import scrapy

class SctrQuotes(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for i in response.css('.titleColumn a'):
            movieName = i.css('::text').get()
            url = i.css('::attr(href)').get()
            dic = {
                'Movie': movieName,
            }
            yield response.follow(url, callback=self.parseMovie, meta=dic)


    def parseMovie(self, response):
            print('\n\n\n\n')
            movieName = response.meta['Movie']
            duration = response.css('.subtext time::text').get().strip()
            genre = ', '.join(response.css('.subtext a:not(:last-child)::text').getall())


            directorName = response.css('h4:contains("Director") + a::text').get()
            directorUrl = response.css('h4:contains("Director") + a::attr(href)').get()

            # print(movieName, duration, genre)

            dic = {
                'Movie Name': movieName,
                'Duration': duration,
                'Genre': genre,
                'Director Name': directorName
            }

            yield response.follow(directorUrl, callback=self.parseDir, meta=dic, dont_filter= True)

    def parseDir(self, response):
        topFourMovies = response.css('.knownfor-title-role a::text').getall()
        topFourMovies = ', '.join(topFourMovies)
        yield {
            'Movie Name': response.meta['Movie Name'],
            'Duration': response.meta['Duration'],
            'Genre': response.meta['Genre'],
            'Director Name': response.meta['Director Name'],
            'Top For Movies': topFourMovies
        }



