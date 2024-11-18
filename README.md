# E-Commerce Flask Application

This is a simple e-commerce web application built using Flask and MongoDB. The application displays products with details such as name, tag, price, and image, fetched dynamically from a MongoDB Atlas database.

## Features
- Displays a homepage with background image, navbar, and footer
- Dynamic products page with product details fetched from MongoDB.
- Responsive UI using Bootstrap for styling.

## Screenshots

Here are some screenshots of the application:

### Code

![Home](static/images/home_code.jpg)

![Product](static/images/products_code.jpg)

### Home Page

![Home Page](static/images/home.jpg)

### Products Page

![Products Page](static/images/products.jpg)

  
## Installation


Follow these steps to set up the project locally:

1. **Clone the repository**:

`git clone https://github.com/your-username/ecommerce-flask-app.git`

2. Navigate to the project directory:
   
`cd ecommerce-flask-app`

4. Install the required dependencies:
   
`pip install -r requirements.txt`

6. Set up your MongoDB Atlas cluster and create a .env file with your connection string:

 `MONGO_URI=your_mongo_uri_here`

8. Run the application:

`python app.py`

10. Open your browser and go to http://127.0.0.1:5000/.

# Running Tests
To ensure the application is functioning as expected, we have written unit tests that cover the following aspects:

- Route Test: Verifies that the routes return the correct HTTP status codes for invalid methods.
- MongoDB Read Operation: Verifies that the MongoDB connection works by pinging the database.
- MongoDB Write Operation: Verifies that data can be successfully written to the MongoDB database.

## Steps to Run Tests Locally
1. Ensure you have installed all dependencies:
`pip install -r requirements.txt`

2. Set up MongoDB credentials as environment variables:
`export MONGODB_URI="your_mongo_uri_"`
`export MONGODB_USERNAME="your_mongodb_username"`
`export MONGODB_PASSWORD="your_mongodb_password"`

3. Run the tests using pytest:
`pytest tests/`

# Screenshots of Passed Tests in Code Editor
## Test Routes
![Test Routes](static/images/PyTest_tests.jpg)

![In Github Actions](static/images/PyTest_CI.jpg)

![TestDBRead]
![TestDBWrite]







