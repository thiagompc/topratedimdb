import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        link = response.xpath('//a[re:test(@href, "/chart/top")]/@href').get()
        yield scrapy.Request(
            response.urljoin(link),
            callback=self.rating_page
        )

    def rating_page(self, response):
        films = response.xpath('//tbody[@class="lister-list"]/tr')
        
        for film in films:
            title = film.xpath('td[@class="titleColumn"]/a/text()').get()
            rating = film.xpath(
                'td[@class="ratingColumn imdbRating"]/strong/text()').get()
            year =  film.xpath(
                'td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()').get() 
            yield{
                'title': title,
                'year': year,
                'rating': rating
        
            }
