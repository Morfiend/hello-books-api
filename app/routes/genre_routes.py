from app import db
from app.models.genre import Genre
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