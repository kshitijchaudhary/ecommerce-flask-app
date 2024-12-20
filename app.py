# Name: Kshitij Chaudhary
# Student ID: c0920457

#importing required libraries
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

mongo_uri = os.getenv('MONGO_URI')

print("connected to",mongo_uri)

# Ensure MongoDB username and password are retrieved
if not mongo_uri:
    raise ValueError("MongoDB credentials are not set in the .env file")


client = MongoClient(mongo_uri)
db = client.shop_db 
products_collection = db.products

# Route for the home page, allowing only GET requests
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Route for the products page
@app.route('/products', methods=['GET'])
def get_products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

# Run the application 
if __name__ == '__main__':
    # Running the app in debug mode for development
    app.run(debug=True)

# Test MongoDB connection (this can be moved to a separate script)
try:
    client.admin.command('ping')
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")