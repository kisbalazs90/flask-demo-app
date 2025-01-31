# Book API Application

This project is a simple Flask-based REST API for managing books using an SQLite database. It includes CRUD (Create, Read, Update, Delete) operations for books. The application uses Flask, Flask-SQLAlchemy, Flasgger for Swagger documentation, and environment variables loaded via `dotenv`.

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flasgger
- python-dotenv

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone this repository to your local machine.
2. Create a `.env` file in the root directory of the project to store your environment variables. Specifically, define the `DATABASE_URI` for the connection to your SQLite database.

Example `.env` file:

```
DATABASE_URI=sqlite:///db.sqlite
```

3. The SQLite database file will be automatically created when you first run the application.

## File Overview

- **app.py**: The main Flask application with routes for managing books.
- **models/book.py**: Contains the `Book` model definition for SQLAlchemy.
- **resources/book/book_service.py**: Includes the logic for handling the various CRUD operations for books (e.g., `book_find_all`, `book_create`).
- **apidocs/swagger.py**: Defines Swagger annotations for API documentation.

## API Endpoints

### 1. **GET /books**

- **Description**: Retrieve a list of all books.
- **Response**: JSON array of all books in the database.
- **Swagger Documentation**: Defined in `GET_BOOKS_ANNOTATION`.

### 2. **POST /books**

- **Description**: Add a new book to the collection.
- **Request Body**: JSON object with the book's details (e.g., title, author, etc.).
- **Response**: JSON object with the newly created book.
- **Swagger Documentation**: Defined in `POST_BOOK_ANNOTATION`.

### 3. **GET /books/<book_id>**

- **Description**: Retrieve a specific book by its ID.
- **Response**: JSON object with the book's details.
- **Swagger Documentation**: Defined in `GET_BOOKS_BY_ID_ANNOTATION`.

### 4. **PUT /books/<book_id>**

- **Description**: Update an existing book's details.
- **Request Body**: JSON object with the updated book information.
- **Response**: JSON object with the updated book.
- **Swagger Documentation**: Defined in `UPDATE_BOOK_ANNOTATION`.

### 5. **DELETE /books/<book_id>**

- **Description**: Delete a book by its ID.
- **Response**: Confirmation message or error message.
- **Swagger Documentation**: Defined in `DELETE_BOOK_ANNOTATION`.

## Running the Application

1. Ensure the `.env` file is configured with the correct database URI.
2. Run the application using the following command:

```bash
python app.py
```

The app will start running on `http://127.0.0.1:5000/` by default.

## Swagger Documentation

The application is integrated with Flasgger to automatically generate Swagger API documentation. To view the documentation, navigate to:

```
http://127.0.0.1:5000/apidocs
```

This will display the interactive API documentation where you can test the endpoints directly.

## Example API Calls

Here are a few examples of how you can interact with the API:

### Create a new book

```bash
curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Book Title", "author": "Author Name"}'
```

### Get all books

```bash
curl -X GET http://127.0.0.1:5000/books
```

### Get a book by ID

```bash
curl -X GET http://127.0.0.1:5000/books/1
```

### Update a book

```bash
curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "Updated Title", "author": "Updated Author"}'
```

### Delete a book

```bash
curl -X DELETE http://127.0.0.1:5000/books/1
```

## Environment Variables

The app loads configuration from environment variables using `python-dotenv`. Below is the required environment variable:

- `DATABASE_URI`: URI for your SQLite database. Example: `sqlite:///books.db`.
