from mongo_connection import connection
import os
import time
from kafka_publisher import produce_weapons

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "users")



def read_all():
    weapons = connection(MONGO_COLLECTION)
    size = weapons.count_documents()
    for i in range(0, size, 40):
        batchs = weapons.find().skip(i).limit(i + 40)
        produce_weapons(batchs)
        time.sleep(0.5)