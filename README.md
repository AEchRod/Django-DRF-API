# Django-DRF-API

## Overview

This repository contains a Django project, showcasing the implementation of a fully functioning RESTful API using Django Rest Framework (DRF) to serve a restaurant called Little Lemon 
so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders. 
The project is structured to provide a foundation for building web APIs with authentication, user management, and other essential features.

## Project Structure

- **LittlelemonAPI:** Django app containing the main functionalities and API endpoints.
- **rest_framework:** Django Rest Framework for building robust APIs.
- **djoser:** A Django REST framework library for user registration, login, and authentication.
- **rest_framework_simplejwt:** Simple JWT-based authentication for Django Rest Framework.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AEchRod/Django-DRF-API.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Configuration

### Settings.py

Key settings in the `settings.py` file include:

- **SECRET_KEY:** Django project secret key. Ensure its security in production.
- **DEBUG:** Debug mode; set to `False` in production.
- **ALLOWED_HOSTS:** List of valid host/domain names for this site.

#### Installed Apps

- `LittlelemonAPI`: Main application for the project.
- `rest_framework`: Django Rest Framework for API development.
- `djoser`: Library for user authentication and registration.
- `rest_framework_simplejwt`: Simple JWT authentication.

#### Database

- Default database: SQLite. Update the `DATABASES` setting for production databases.

#### Static Files

- `STATIC_URL`: URL to serve static files.

#### REST_FRAMEWORK Settings

- **DEFAULT_RENDERER_CLASSES:** JSONRenderer and BrowsableAPIRenderer for admin and browsable API views.
- **DEFAULT_AUTHENTICATION_CLASSES:** TokenAuthentication, SessionAuthentication, and JWTAuthentication for user authentication.

#### DJOSER Settings

- **USER_ID_FIELD:** Specifies the user model field acting as the primary key.

## Usage

Explore the API endpoints and functionalities provided by the LittlelemonAPI app. Use the provided authentication mechanisms for user management and secure API access.

## Contributing

Feel free to contribute by opening issues, providing feedback, or submitting pull requests. Contributions are welcome and appreciated.
