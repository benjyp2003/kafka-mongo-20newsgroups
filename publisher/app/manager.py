from publisher.app.data_loader import DataLoader
from publisher.app.kafka_producer import Producer


class Manager:
    def __init__(self, interesting_topic = "interesting_categories", not_interesting_topic = "not_interesting_categories"):
        self.producer = Producer()
        self.data_loader = DataLoader()
        self.interesting_data = self.get_interesting_data()
        self.not_interesting_data = self.get_not_interesting_data()
        self.interesting_topic = interesting_topic
        self.not_interesting_topic = not_interesting_topic
        self.interesting_categories = [
                                        'alt.atheism',
                                        'comp.graphics',
                                        'comp.os.ms-windows.misc',
                                        'comp.sys.ibm.pc.hardware',
                                        'comp.sys.mac.hardware',
                                        'comp.windows.x',
                                        'misc.forsale',
                                        'rec.autos',
                                        'rec.motorcycles',
                                        'rec.sport.baseball'
                                    ]
        self.not_interesting_topic = [
                                        'rec.sport.hockey',
                                        'sci.crypt',
                                        'sci.electronics',
                                        'sci.med',
                                        'sci.space',
                                        'soc.religion.christian',
                                        'talk.politics.guns',
                                        'talk.politics.mideast',
                                        'talk.politics.misc',
                                        'talk.religion.misc'
                                    ]


    def get_interesting_data(self) -> list:
        return self.data_loader.load_interesting_newsgroups()

    def get_not_interesting_data(self) -> list:
        return self.data_loader.load_not_interesting_newsgroups()


    def extract_one_interesting_article_per_cat(self):
        interesting_articles = {}

        for category in self.interesting_categories:
            for article in self.interesting_data:
                if article.get('category') == category and category not in interesting_articles:
                    interesting_articles[category] = article
                    self.interesting_data.remove(article)

        return interesting_articles

    def extract_one_not_interesting_article_per_cat(self):
        not_interesting_articles = {}

        for category in self.not_interesting_topic:
            for article in self.not_interesting_data:
                if article.get('category') == category and category not in not_interesting_articles:
                    not_interesting_articles[category] = article
                    self.not_interesting_data.remove(article)

        return not_interesting_articles

    def publish(self):
        self.producer.publish(topic=self.interesting_topic, event=self.extract_one_interesting_article_per_cat())
        self.producer.publish(topic=self.not_interesting_topic, event=self.extract_one_not_interesting_article_per_cat())