from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fake Title", "A made-up book."),
    Book(2, "Another Fake Title", "The sequel to the original book that wasn't!"),
    Book(3, "A Real Book?", "Don't believe the lies!")
]

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)


@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Morgan",
        "message": "Yooooo",
        "hobbies": ["gaming", "reading", "motorcycles"]
    }

@hello_world_bp.route("/not-broken")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body