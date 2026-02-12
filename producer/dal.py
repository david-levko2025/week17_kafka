import os
import time

from mongo_connection import MongoConnector
from kafka_publisher import produce_connection

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "users")
connection = MongoConnector()


def read_all_connection():
    conn = connection.get_coll(MONGO_COLLECTION)
    size = conn.count_documents()
    for i in range(0, size, 40):
        batches = conn.find().skip(i).limit(i + 40)
        produce_connection(batches)
        time.sleep(0.5)