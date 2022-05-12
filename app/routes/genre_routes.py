from app import db
from app.models.genre import Genre
from app.models.book import Book
from app.helpers import validate_genre
from flask import Blueprint, jsonify, request

genres_bp = Blueprint("genres", __name__, url_prefix="/genres")

@genres_bp.route("", methods=["POST"])
def create_genre():
    request_body = request.get_json()

    new_genre = Genre(name=request_body["name"])

    db.session.add(new_genre)
    db.session.commit()

    return jsonify(f"Genre {new_genre.name} successfully created"), 201

@genres_bp.route("", methods={"GET"})
def get_all_genres():
    genres = Genre.query.all()

    genres_response = []
    for genre in genres:
        genres_response.append(
            {"id": genre.id,
            "name": genre.name}
        )
    
    return jsonify(genres_response), 200

@genres_bp.route("/<genre_id>/books", methods=["POST"])
def create_book(genre_id):
    genre = validate_genre(genre_id)

    request_body = request.get_json()

    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author_id=request_body["author_id"],
        genres=[genre]
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(f"Book {new_book.title} by {new_book.author.name}"\
        " successfully created"), 201

@genres_bp.route("/<genre_id>/books", methods=["GET"])
def get_all_books(genre_id):
    genre = validate_genre(genre_id)

    books_response = []
    for book in genre.books:
        books_response.append(book.to_dict())

    return jsonify(books_response), 200