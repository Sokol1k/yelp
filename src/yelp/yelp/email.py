from scrapy.mail import MailSender
from yelp.settings import MAIL_HOST, MAIL_PORT, MAIL_FROM, MAIL_PASS, MAIL_USER, MAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pprint


class EmailPipline(object):

    def close_spider(self, spider):
        subject = "Yelp Parse"
        to_email = MAIL_TO
        body = spider.crawler.stats.get_stats()
        body = pprint.pformat(body)
        body = "Yelp.com site parser result: \n\n" + body
        mailer = MailSender(smtphost=MAIL_HOST, mailfrom=MAIL_FROM,
                            smtpuser=MAIL_USER, smtppass=MAIL_PASS, smtpport=MAIL_PORT)
        return mailer.send(to=[to_email], subject=subject, body=body)
