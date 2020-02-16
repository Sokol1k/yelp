import scrapy
from yelp.items import YelpItem

host = "https://www.yelp.com"

class YelpSpider(scrapy.Spider):
    name = 'yelp'

    def start_requests(self):
        category = getattr(self, 'category', 'Restaurants')
        location = getattr(self, 'location', 'Los Angeles, CA')
        url = f'{host}/search?find_desc={category}&find_loc={location}'
        # yield scrapy.Request(url=url, callback=self.parse)
        yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': 'http://192.168.11.82:9966'})

    def parse(self, response):
        for url in response.xpath('//h3/span/a/@href'):
            if not url:
                continue
            yield scrapy.Request(url=f'{host}{url.get()}', callback=self.parse_business)
        next_page_url = response.xpath(
            '//div[@class="lemon--div__373c0__1mboc navigation-button-container__373c0__spUng border-color--default__373c0__2oFDT"]/a/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_business(self, response):
        name = response.xpath('//h1/text()').get()
        if not name:
            return
        category = self.category_processing(response.xpath(
            '//div[@class="lemon--div__373c0__1mboc u-space-b3 border-color--default__373c0__2oFDT"]/div/span[2]'))
        address = self.address_processing(response.xpath('//address[1]'))
        phone = response.xpath(
            '//div[@class="lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT"]/p[2]/text()').get()
        reviews = self.reviews_processing(response.xpath(
            '//div[@class="lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-6__373c0__zqA5A vertical-align-middle__373c0__2TQsQ u-space-b1 border-color--default__373c0__2oFDT"]//p/text()').get())
        rating = self.rating_processing(response.xpath(
            '//div[@class="lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-6__373c0__zqA5A vertical-align-middle__373c0__2TQsQ u-space-b1 border-color--default__373c0__2oFDT"]/div[1]//div/@aria-label').get())
        image = response.xpath(
            '(//img[@class="lemon--img__373c0__3GQUb"])[2]/@src').get()
        site = response.xpath('//div[@class="lemon--div__373c0__1mboc island__373c0__3fs6U u-padding-t1 u-padding-r1 u-padding-b1 u-padding-l1 border--top__373c0__19Owr border--right__373c0__22AHO border--bottom__373c0__uPbXS border--left__373c0__1SjJs border-color--default__373c0__2oFDT background-color--white__373c0__GVEnp"]/div[1]//a/text()').get()
        workdays = self.workdays_processing(response.xpath('//tbody'))
        yield YelpItem(**{
            'name': name,
            'category': category,
            'address': address,
            'phone': phone,
            'reviews': reviews,
            'rating': rating,
            'image_urls': [image],
            'site': site,
            'workdays': workdays
        })

    def address_processing(self, data):
        address = ''
        for elem in data.xpath('.//p/span/text()'):
            address += str(elem.get()) + ' '
        address = address.rstrip()
        return address

    def category_processing(self, data):
        category = ''
        for elem in data.xpath('.//span/a/text()'):
            category += str(elem.get()) + ', '
        category = category.rstrip(', ')
        return category

    def reviews_processing(self, data):
        reviews = str(data)
        reviews = reviews.split(' ')[0]
        return reviews

    def rating_processing(self, data):
        rating = str(data)
        rating = rating.split(' ')[0]
        return rating

    def workdays_processing(self, data):
        workdays = {}
        for elem in data.xpath('.//tr'):
            day = elem.xpath('.//th/p/text()').get()
            time = ''
            for item in elem.xpath('.//td/ul/li'):
                time += str(item.xpath('.//p/text()').get()) + ', '
            time = time.rstrip(', ')
            workdays[day] = time
        return workdays

# python start-parse.py Restaurants Los Angeles, CA
# scrapy crawl yelp
# scrapy crawl yelp --output=data.json -L WARNING
