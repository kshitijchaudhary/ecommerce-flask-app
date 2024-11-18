import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables for MongoDB credentials
load_dotenv()

class TestDatabase(unittest.TestCase):
    
    def test_mongo_write_operation(self):
        mongo_uri = os.getenv('MONGO_URI')

        # Ensure MongoDB username and password are retrieved
        if not mongo_uri:
            raise ValueError("MongoDB credentials are not set in the .env file")
        
        client = MongoClient(mongo_uri)

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
