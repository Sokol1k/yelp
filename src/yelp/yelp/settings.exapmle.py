BOT_NAME = 'yelp'

SPIDER_MODULES = ['yelp.spiders']
NEWSPIDER_MODULE = 'yelp.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

IMAGES_STORE = '../image'

ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'yelp.pipelines.YelpPipeline': 2,
   'yelp.email.EmailPipline': 3
}

MAIL_HOST = ''
MAIL_PORT = ''
MAIL_FROM = ''
MAIL_USER = ''
MAIL_PASS = ''
MAIL_TO = ''
