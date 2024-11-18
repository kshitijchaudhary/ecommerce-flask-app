import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestFlaskApp(unittest.TestCase):
    
    # Test to check if the home route is accessible via GET
    def test_home_route_get(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)  # Home page should return 200 OK
            
    # Test to check if products route is accessible via GET
    def test_products_route_get(self):
        with app.test_client() as client:
            response = client.get('/products')
            self.assertEqual(response.status_code, 200)  # Products page should return 200 OK

if __name__ == "__main__":
    unittest.main()
