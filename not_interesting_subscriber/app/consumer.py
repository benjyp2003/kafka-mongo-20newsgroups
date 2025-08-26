from datetime import datetime, timezone

from kafka import KafkaConsumer
import json

class Consumer:

    @staticmethod
    def get_consumer_events(topic = ''):
        # The consumer object contains the topic name, json deserializer,Kafka servers
        # and kafka time out in ms, Stops the iteration if no message after 1 sec
        consumer = KafkaConsumer(topic,
                                 group_id='not-interesting-subscriber-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=['localhost:9092'],
                                 consumer_timeout_ms=10000)
        return consumer


    def consume_messages(self, topic: str = "not_interesting_categories"):
        try:
            events = self.get_consumer_events(topic)
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
