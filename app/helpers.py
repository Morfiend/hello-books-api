from flask import abort, make_response
from .models.book import Book
from .models.author import Author
from .models.genre import Genre

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))

    return book

def validate_author(author_id):
    try:
        author_id = int(author_id)
    except:
        abort(make_response({"message":f"author {author_id} invalid"}, 400))

    author = Author.query.get(author_id)

    if not author:
        abort(make_response({"message":f"author {author_id} not found"}, 404))

    return author

def validate_genre(genre_id):
    try:
        genre_id = int(genre_id)
    except:
        abort(make_response({"message":f"Genre {genre_id} invalid"}, 400))

    genre = Genre.query.get(genre_id)

    if not genre:
        abort(make_response({"message":f"Genre {genre_id} not found"}, 404))

    return genre