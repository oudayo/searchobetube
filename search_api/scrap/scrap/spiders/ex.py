
import scrapy
import json

class ScrapoSpider(scrapy.Spider):
    name = "scrapo"
    allowed_domains = ["www.googleapis.com"]

    def start_requests(self):
        urls = [f"https://www.googleapis.com/customsearch/v1?q={self.query} cdfor {self.level} &key=AIzaSyCIKEESnF7bt6Zu5HmM2S58amw5BddUm8M&cx=c7e776d141aa547c6&start=1&gl=us",]


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        resp = json.loads(response.text)
        items = resp.get('items')
        next_pages = resp.get('nextPage', [])


        for next_page in resp.get('queries', {}).get('nextPage', []):
            for item in items :
                for metatag in item.get('pagemap', {}).get('metatags', []):



                    yield{
                        'Course_name': item.get('title'),
                        'Snippet': item.get('snippet'),
                        'Link': item.get('link'),
                        'images':metatag.get('og:image'),
                        'totalResults':next_page.get('totalResults'),
                        'count':next_page.get('count'),
                        'startIndex' : next_page.get('startIndex')




                }




