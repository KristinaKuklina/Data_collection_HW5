import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["m.imdb.com"]
    start_urls = ["https://m.imdb.com/list/ls066758419/"]

    def parse(self, response):
        films = response.xpath("//span[@class='media-body media-vertical-align lister-item-content']")
        for film in films:
            film_title = film.xpath(".//span[@class='h4']/text()").get()
            runtime = film.xpath(".//span[@class='runtime']/text()").get()
            genre = film.xpath(".//span[@class='genre']/text()").get().strip()
            rating = film.xpath(".//span[@class='imdb-rating']/text()").get()
            yield {
                'film_title' : film_title,
                'runtime' : runtime,
                'genre' : genre,
                'rating' : rating
                }
