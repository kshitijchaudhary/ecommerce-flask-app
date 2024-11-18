import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables for MongoDB credentials
load_dotenv()

class TestDatabase(unittest.TestCase):
    
    def test_mongo_write_operation(self):
        MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
        MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
        
        # Connect to MongoDB
        client = MongoClient(f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.deqr1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client.shop_db
        collection = db.products
        
        # Insert a test document
        test_document = {"name": "test_item", "price": 10}
        result = collection.insert_one(test_document)
        
        # Verify the document was inserted
        inserted_document = collection.find_one({"name": "test_item"})
        self.assertIsNotNone(inserted_document)
        self.assertEqual(inserted_document["price"], 10)

if __name__ == "__main__":
    unittest.main()
