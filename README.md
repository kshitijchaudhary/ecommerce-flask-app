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

![Products Page](static/images/products.png)

### Product Detail

![Product Detail](static/images/product_detail_screenshot.png)
  
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


