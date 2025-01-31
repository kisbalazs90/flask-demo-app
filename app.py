# app.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask import Flask, request, jsonify
from flasgger import Swagger
from dotenv import load_dotenv
import os
from resources.book.book_model import Book
from resources.book.book_service import book_find_all, book_find_one, book_create, book_update, book_delete
from apidocs.swagger import *

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)

db.init_app(app)

@app.route('/books', methods=['GET'])
def get_books():
  return book_find_all()
get_books.__doc__ = GET_BOOKS_ANNOTATION

@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()
  return book_create(data)
add_book.__doc__ = POST_BOOK_ANNOTATION

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
  book_find_one(book_id)
get_book.__doc__ = GET_BOOKS_BY_ID_ANNOTATION

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  data = request.get_json()
  return book_update(book_id, data)
update_book.__doc__ = UPDATE_BOOK_ANNOTATION

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return book_delete(book_id);
delete_book.__doc__ = DELETE_BOOK_ANNOTATION

if __name__ == '__main__':
    app.run(debug=True)
