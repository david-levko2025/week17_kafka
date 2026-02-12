from pymongo import MongoClient
from os import getenv

mongo_uri = getenv('MONGO_URI', 'mongodb://localhost:27017')
mongo_db = getenv('MONGO_DB', 'week17')
mongo_collerction = getenv('MONGO_COLLECTION', 'testercollection')
file_patch = './suspicious_customers_orders.json'

def get_connection():
    client = MongoClient(mongo_uri)
    db = client["concats_data"]
    collection = db["usersAndCustomers"]
    return collection

collection = get_connection()