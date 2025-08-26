import os
from pymongo import MongoClient, errors


class Dal:
    def __init__(self, collection_name: str = "not-interesting-articles"):
        self.client = None
        self.db = None
        self.database_name = os.getenv("MONGO_DATABASE", "news-articles")
        self.mongo_host = os.getenv("MONGO_HOST", "mongodb")
        self.mongo_port = os.getenv("MONGO_PORT", "27017")
        self.uri = f"mongodb://{self.mongo_host}:{self.mongo_port}/"
        self.collection_name = collection_name


    def fetch_all_docs(self):
        """ Fetch all documents from a MongoDB collection."""
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database_name]
                collection = self.db[self.collection_name]
                result = list(collection.find({}, {"_id": 0}))
                return result

        except errors.PyMongoError as e:
            raise Exception(f"Error fetching docs from {collection} collection: {e}")

    def insert_doc(self, doc):
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database_name]
                collection = self.db[self.collection_name]
                collection.insert_one(doc)

        except errors.PyMongoError as e:
            raise Exception(f"Error inserting docs into {collection} collection: {e}")
        except Exception as e:
            raise Exception(f"Error inserting docs into {collection} collection: {e}")
