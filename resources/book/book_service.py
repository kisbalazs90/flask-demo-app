from resources.book.book_model import Book
from flask import jsonify

def book_find_all():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year} for book in books])

def book_create(data):
    new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'title': new_book.title, 'author': new_book.author, 'published_year': new_book.published_year}), 201

def book_find_one(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year})

def book_update(book_id, data):
    book = Book.query.get_or_404(book_id)
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.published_year = data.get('published_year', book.published_year)
    db.session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year})

def book_delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})