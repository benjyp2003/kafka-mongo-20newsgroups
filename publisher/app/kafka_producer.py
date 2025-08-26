
from kafka import KafkaProducer
import json


class Producer:
    def __init__(self):
        self.producer = self.get_producer_config()


    def publish_message_with_key(self, topic,key, message):
        self.producer.send(topic, key=key, value=message)

    def get_producer_config(self):
        # The Producer object requires the Kafka server, Json serializer
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer

    def publish(self,   topic, event):
        self.producer.send(topic, event)


    def flush(self):
        self.producer.flush()


