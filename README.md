# E-commerce Flask Application

An e-commerce web application built with Flask, designed to allow users to browse and purchase products. The app includes features for managing user profiles, product categories, carts, favorites, and admin functionalities like product management and uploading images.

## Project Links

- **Deployed Site**: [E-commerce Web Application](https://developmentenv.tech/home).
- **GitHub Repository**: [Project GitHub](https://github.com/vergilx6x/E-commerce-website-v2.git).
- **Landing Page**: [Landing Page](https://vergilx6x.github.io/E-commerce-website/).
- **Author LinkedIn**: [Mohamed Amine Thami](https://www.linkedin.com/in/mohamed-amine-thami-526b9b280/).

## Introduction

This application offers a fully functional e-commerce platform where users can:

- Browse products across different categories.
- Add items to their shopping cart.
- Mark products as favorites for easy access later.
- Manage their profiles with options to upload profile pictures.
- Admin users can manage products, categories, and users and upload product images.

## Features
- **User Authentication**: Register, log in, and manage user profiles.
- **Product Management**: Admins can add, edit, delete products, and upload product images.
- **Cart Management**: Users can manage their shopping cart by adding and removing products.
- **Favorites**: Add products to a favorites list for future reference.
- **Category Browsing**: Products are categorized for easier browsing.
- **Admin Panel**: Manage products, categories, users, and images.
- **Responsive Design**: Built with Bootstrap 5, ensuring a responsive and modern user interface.

## Project Structure

```bash
.
├── main.py
├── models/
│   ├── base_model.py
│   ├── cart.py
│   ├── category.py
│   ├── product.py
│   ├── user.py
│   └── ...
├── web_flask/
│   ├── app.py
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── uploads/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── ...
│   └── ...
└── setup_db.sh

```

## Installation

- 1- Clone the repository:
```bash
git clone https://github.com/vergilx6x/E-commerce-website.git
cd E-commerce-website
```

- 2- Install Python 3 (if not already installed):
  - [Python Installation Guide](https://www.python.org/downloads/).

- 3- Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

- 4- Install required packages:
```bash
pip install -r requirements.txt
```
- 5- Install MySQL (if not installed):
  - Follow instructions for your operating system on the [MySQL installation page](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).

- 6- Set up the database:
  - Modify your database credentials in the config file (ensure your MySQL server is running).
```bash
bash setup_db.sh
```

- 7- Run the Flask application:
```bash
python3 -m run.py
```
- 8- Access the app:
  - Visit: http://localhost:5000
  
## Usage

- **User Registration**: Sign up for an account to browse products, manage your shopping cart, and save favorite products.
- **Admin Features**: Log in as an admin to access the admin panel for managing products, categories, and users.
- **Cart Management**: Users can add products to the cart, update quantities, or remove items.
- **Favorites**: Easily mark and manage favorite products.

## Contributing
- 1- Fork the repository.
- 2- Create your feature branch: git checkout -b feature/AmazingFeature
- 3- Commit your changes: git commit -m 'Add some AmazingFeature'
- 4- Push to the branch: git push origin feature/AmazingFeature
- 5- Open a pull request.

## Related Projects
- Flask-Admin - Admin interface for Flask apps.
- Flask-Login - User session management for Flask.

## Licensing

This project is licensed under the MIT License - see the LICENSE file for details.

## Screenshots:

![Product screenshot](.app/static/images/home_page1.png)