from app import db
from app.helpers import validate_author
from app.models.author import Author
from app.models.book import Book
from flask import Blueprint, jsonify, request

authors_bp = Blueprint("authors", __name__, url_prefix="/authors")

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name=request_body["name"])

    db.session.add(new_author)
    db.session.commit()

    return jsonify(f"Author {new_author.name} successfully created"), 201

@authors_bp.route("", methods=["GET"])
def get_all_authors():
    authors = Author.query.all()

    author_response = []
    for author in authors:
        author_response.append(author.to_json())

    return jsonify(author_response), 200

@authors_bp.route("/<author_id>/books", methods=["POST"])
def create_book(author_id):
    author = validate_author(author_id)

    request_body = request.get_json()

    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author=author
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(f"Book {new_book.title} by {new_book.author.name}"\
        " successfully created"), 201

@authors_bp.route("/<author_id>/books", methods=["GET"])
def get_all_books(author_id):
    author = validate_author(author_id)

    books_response = []
    for book in author.books:
        books_response.append(book.to_json())

    return jsonify(books_response), 200
