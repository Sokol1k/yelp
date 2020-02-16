from sqlalchemy.orm import sessionmaker
from yelp.models import Business, db_connect


class YelpPipeline(object):
    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()

        business = session.query(Business).filter_by(name=item['name']).first()

        if not business:
            business = Business()
            business.name = item['name']

        business.category = item['category']
        business.address = item['address']
        business.phone = item['phone']
        business.reviews = item['reviews']
        business.rating = item['rating']
        business.image = item['images'][0]['path']
        business.site = item['site']
        business.workdays = item['workdays']

        try:
            session.add(business)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
