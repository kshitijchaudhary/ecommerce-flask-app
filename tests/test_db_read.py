import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables for MongoDB credentials
load_dotenv()

class TestDatabase(unittest.TestCase):
    
    def test_mongo_read_connection(self):
        MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
        MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
        
        # Connect to MongoDB
        client = MongoClient(f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.deqr1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        
        # Test MongoDB connection
        try:
            client.admin.command('ping')
            print("MongoDB connection successful!")
        except Exception as e:
            self.fail(f"MongoDB connection failed: {e}")

if __name__ == "__main__":
    unittest.main()
