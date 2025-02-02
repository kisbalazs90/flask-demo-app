# app.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from apidocs.swagger import *
from dotenv import load_dotenv
from flasgger import Swagger
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from resources.book.book_model import Book
from resources.book.book_service import book_find_all, book_find_one, book_create, book_update, book_delete
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')

db.init_app(app)

with app.app_context():
    db.create_all()

jwt = JWTManager(app)
swagger = Swagger(app, config=swagger_config)

@app.route("/login", methods=["POST"])
def login():
    built_in_user = os.getenv('USER_NAME')
    built_in_password = os.getenv('USER_PASSWORD')
    print(built_in_user, built_in_password)

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != built_in_user or password != built_in_password:
        return {"msg": "Bad username or password"}, 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
login.__doc__ = LOGIN_ANNOTATION


@app.route('/books', methods=['GET'])
@jwt_required()
def get_books():
  return book_find_all()
get_books.__doc__ = GET_BOOKS_ANNOTATION

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
  book_find_one(book_id)
get_book.__doc__ = GET_BOOKS_BY_ID_ANNOTATION

@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
  data = request.get_json()
  return book_create(data)
add_book.__doc__ = POST_BOOK_ANNOTATION

@app.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
  data = request.get_json()
  return book_update(book_id, data)
update_book.__doc__ = UPDATE_BOOK_ANNOTATION

@app.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    return book_delete(book_id);
delete_book.__doc__ = DELETE_BOOK_ANNOTATION



if __name__ == '__main__':
    app.run(debug=True)
