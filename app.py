#importing required libraries
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGO_URI'))
db = client.shop_db 
products_collection = db.products

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the products page
@app.route('/products')
def get_products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

# Run the application 
if __name__ == '__main__':
#Running the app in debug mode for development
    app.run(debug = True)