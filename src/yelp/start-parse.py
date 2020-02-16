import argparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from yelp.spiders.yelp_spider import YelpSpider

parse = argparse.ArgumentParser(description="Enter parsing data for yelp.com")
parse.add_argument('category', metavar='category', type=str,)
parse.add_argument('location', metavar='location', type=str,)

arguments = parse.parse_args()

process = CrawlerProcess(get_project_settings())
process.crawl(YelpSpider,
              category=arguments.category,
              location=arguments.location)
process.start()
