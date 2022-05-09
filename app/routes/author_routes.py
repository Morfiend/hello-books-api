from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request

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