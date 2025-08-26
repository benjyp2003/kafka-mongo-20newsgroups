from datetime import datetime, timezone

from .consumer import Consumer
from .dal import Dal


class Manager:
    def __init__(self):
        self.consumer = Consumer
        self.dal = Dal()

    def consume_messages(self, topic: str = "not-interesting_categories"):
            try:
                events = self.consumer.get_consumer_events(topic)
                all_messages = []
                for msg in events:
                    doc = {
                        "topic": msg.topic,
                        "partition": msg.partition,
                        "offset": msg.offset,
                        "key": msg.key.decode("utf-8") if msg.key else None,
                        "value": msg.value,
                        "ts": datetime.now(timezone.utc),  # receipt timestamp (UTC, tz-aware)
                    }
                    all_messages.append(doc)

                return all_messages

            except Exception as e:
                raise Exception(f"Error consuming messages from topic {topic}: {e}")

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