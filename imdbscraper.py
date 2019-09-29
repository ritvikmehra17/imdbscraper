from scrapy import Spider

class Imdb(Spider):
    name="moviespider"
    start_urls=['https://www.imdb.com/movies-in-theaters/']

    def parse(self,response):
       
        cards=response.css("div.list_item")
        print("found total ",len(cards),"item")
        
        for item in cards:
            title = item.css("h4 a::text").extract_first()
            duration = item.css("time::text").extract_first()
            metascore = item.css("span.metascore::text").extract_first()
            outline = item.css("div.outline::text").extract_first()
            blocks = item.css("div.txt-block")
            director = blocks[0].css("span a::text").extract_first() #extract_first as string
            actors=blocks[1].css("span a::text").extract() #extract as a list
            actors=",".join(actors)
            yield{
                'title':title,'duration':duration,
                'metascore':metascore, 'outline':outline,
                'director':director, 'actors':actors
            }

