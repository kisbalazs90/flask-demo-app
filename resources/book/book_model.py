# models/book.py
from app import db
from flask_sqlalchemy import SQLAlchemy

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
