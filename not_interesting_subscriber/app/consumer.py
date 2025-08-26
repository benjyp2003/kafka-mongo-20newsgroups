from datetime import datetime, timezone

from kafka import KafkaConsumer
import json

class Consumer:

    @staticmethod
    def get_consumer_events(topic):
        """Returns a Kafka consumer for the specified topic."""
        # The consumer object contains the topic name, json deserializer,Kafka servers
        consumer = KafkaConsumer(topic,
                                 group_id='not-interesting-subscriber-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=['kafka:9092'],
                                 auto_offset_reset='earliest')
        return consumer



