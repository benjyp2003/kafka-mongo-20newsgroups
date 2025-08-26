from datetime import datetime, timezone

from .consumer import Consumer
from .dal import Dal


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.dal = Dal()

    def process_messages(self, topic: str):
        try:
            event = self.consumer.get_consumer_events(topic)
            for msg in event:
                # msg.value contains the dictionary with 10 categories
                categories_dict = msg.value

                # Iterate through each category and save separately
                for category_name, article_data in categories_dict.items():
                    doc = {
                        "topic": msg.topic,
                        "partition": msg.partition,
                        "offset": msg.offset,
                        "key": msg.key.decode("utf-8") if msg.key else None,
                        "category": category_name,
                        "article": article_data,
                        "time_stamp": datetime.now(timezone.utc),  # receipt timestamp (UTC, tz-aware)
                    }
                    self.dal.insert_doc(doc)
        except Exception as e:
            raise Exception(f"Error consuming messages from topic {topic}: {e}")


    def get_articles(self):
            try:
                articles = self.dal.fetch_all_docs()
                return {"articles": articles}
            except Exception as e:
                raise Exception(f"Error retrieving interesting articles from DB: {e}")