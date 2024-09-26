# Customer Orders API

A Django-based API for managing customers and orders with OAuth2 authentication and Africa's Talking SMS notifications.

## Features
- Customers and orders management (CRUD)
- OAuth2 authentication and authorization
- Sends SMS notifications via Africa's Talking when an order is created
- PostgreSQL as the database
- CI/CD pipeline using GitHub Actions and Google App Engine for deployment

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- **Python 3.10**
- **PostgreSQL**
- **Africa's Talking Account** (for SMS functionality)
- **Google Cloud Account** (for deployment)

---

## Setup Instructions

### 1. **Clone the Repository**
To start, clone the project repository to your local machine.

### 2. **Set Up a Virtual Environment**
To manage dependencies, create a virtual environment and activate it.

### 3. **Install Dependencies**
Once the environment is activated, install all necessary packages using the requirements.txt file.

### 4. **Configure Environment Variables**
The project requires some environment variables to be set. These values will be read from a `.env` file.

### 5. **Set Up the Database**
Ensure PostgreSQL is installed and running. Create the database that will be used for the project.

### 6. **Run Migrations**
Run Django migrations to set up the database schema.

### 7. **Run the Django Development Server**
To run the server locally.

### 8. **Create a Superuser**
To access the Django Admin interface for managing customers and orders, create a superuser.

---

## API Endpoints

After setting up the server, you can interact with the API using Postman or any other API testing tool.

### Authentication
Before using any of the protected endpoints (e.g. for creating customers or orders), you need to obtain an OAuth2 token.

### Customers API
1. **Create a Customer**  
2. **List Customers**

### Orders API
1. **Create an Order**  
2. **List Orders**

---

## Running Tests

To run the unit tests for the project, use a coverage tool to run tests and generate a coverage report.

---

## Postman API Testing Guide

1. **Install Postman**: Download and install Postman.
2. **Set up OAuth2 token**:
   - Go to the Postman Authorization tab and input your client credentials to obtain an access token.
3. **Test the API Endpoints**:
   - Start by testing the customer and order creation endpoints.
   - Test order creation and check if SMS notifications are sent successfully.

---

## Deployment to Google App Engine

### 1. **Configure Google Cloud**
Ensure the Google Cloud SDK is installed and authenticated.

### 2. **App Configuration**
Ensure your `app.yaml` and `deploy.yml`files are correctly set up for App Engine deployment.

### 3. **Deploy to Google App Engine**
Deploy the app using Google Cloud CLI.

---

## CI/CD with GitHub Actions

GitHub Actions is set up to automate testing and deployment. Pushing code to the `main` branch will:
   - Install dependencies
   - Run tests with coverage
   - Deploy the application to Google App Engine

---