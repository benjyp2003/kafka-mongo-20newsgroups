
from .consumer import Consumer
from .dal import Dal


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.dal = Dal()




    def save_messages_to_db(self, messages: dict):
        try:
            for message in messages:
                self.dal.insert_doc(message)
        except Exception as e:
            raise Exception(f"Error saving messages to DB: {e}")

    def get_articles(self):
        try:
            articles = self.dal.fetch_all_docs()
            return articles
        except Exception as e:
            raise Exception(f"Error retrieving articles from DB: {e}")