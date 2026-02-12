from pymongo import MongoClient
import os

    
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
mongo_db = os.getenv('MONGO_DB', 'users_db')
mongo_collection = os.getenv('MONGO_COLLECTION', 'testercollection')
file_patch = './suspicious_customers_orders.json'

def get_connection():
    client = MongoClient(mongo_uri)
    db = client["concats_data"]
    collection = db["usersAndCustomers"]
    return collection

connection = get_connection()