from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request
from .helpers import validate_book

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter(Book.title.ilike(f"%{title_query}%"))
    else:
        books = Book.query.all()

    books_response = []
    for book in books:
        books_response.append(book.to_json())

    return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)

    return jsonify(book.to_json()), 200

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully updated"), 200)

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"), 200)