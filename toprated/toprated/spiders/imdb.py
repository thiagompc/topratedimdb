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
        films = response.xpath('//tr').getall()

        for film in films:
            title = response.xpath(
                '//tr//td[@class="titleColumn"]/a/text()').getall()
            rating = response.xpath(
                '//tr//td[@class="ratingColumn imdbRating"]/strong/text()').getall()
        yield{
            'title': title,
            'rating': rating
        }
        import pdb; pdb.set_trace()
        pass
