
# Book API with JWT Authentication

This project implements a basic Book Management API using Flask. The API supports JWT authentication to secure certain endpoints. The project uses Flasgger to generate Swagger UI for the API documentation.

## Features

- **Authentication**: JWT-based authentication for accessing secure endpoints.
- **CRUD Operations for Books**: You can create, read, update, and delete books via the API.
- **Swagger UI**: Auto-generated API documentation with Flasgger for easy interaction with the API.

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flasgger
- dotenv (for environment variables)

## Installation

1. Clone this repository:

   ```bash
   git clone https://your-repo-url.git
   cd your-repo-folder
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root of the project and set the following values:

   ```env
   FLASK_ENV=development
   DATABASE_URI=sqlite:///db.sqlite
   USER_NAME=admin
   USER_PASSWORD=admin
   JWT_SECRET=your_generated_jwt_secret_key
   ```

## Usage

1. **Start the application**:

   ```bash
   python app.py
   ```

   The app will start running on `http://127.0.0.1:5000/`.

2. **Swagger UI**:

   The Swagger UI documentation can be accessed at `http://127.0.0.1:5000/apidocs/`.

3. **Login and Get JWT Token**:

   To access secure endpoints, you must first log in and get the JWT token:

   - **Endpoint**: `POST /login`
   - **Body**:
     ```json
     {
       "username": "admin",
       "password": "admin"
     }
     ```

   - On successful login, you will receive a JWT token:

     ```json
     {
       "access_token": "your-jwt-token-here"
     }
     ```

4. **Use JWT Token to Access Secured Endpoints**:

   - **Add `Authorization: Bearer <your-jwt-token-here>` header** to make requests to the protected endpoints like `/books`.

## Endpoints

- **POST /login**: Authenticates the user and returns a JWT token.
- **GET /books**: Retrieves all books (requires JWT authentication).
- **GET /books/{book_id}**: Retrieves a book by ID (requires JWT authentication).
- **POST /books**: Adds a new book (requires JWT authentication).
- **PUT /books/{book_id}**: Updates a book by ID (requires JWT authentication).
- **DELETE /books/{book_id}**: Deletes a book by ID (requires JWT authentication).

## Example cURL Requests

- **Login Request**:

  ```bash
  curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'
  ```

- **Get All Books** (Authenticated):

  ```bash
  curl -X GET http://127.0.0.1:5000/books -H "Authorization: Bearer <your-jwt-token-here>"
  ```

