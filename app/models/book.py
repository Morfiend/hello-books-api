from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, ForeignKey('author.id'))
    author = relationship("Author", back_populates="books")

    def to_json(self):
        return {
        "id": self.id,
        "title": self.title,
        "description":self.description
        }