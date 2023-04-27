from scrapy.crawler import CrawlerProcess

import argparse
import scrap.spiders.ex as sc


parser = argparse.ArgumentParser()

parser.add_argument("--query")
parser.add_argument("--level")

args = parser.parse_args()

process = CrawlerProcess(settings={
    "FEEDS": {
        "resultat.json": {"format": "json"},
    },
})

levels = {
    "1": "kids",
    "2": "beginner",
    "3": "intermediate",
    "4": "expert",
}
process.crawl(sc.ScrapoSpider, query=args.query, level=levels[args.level])
process.start()





