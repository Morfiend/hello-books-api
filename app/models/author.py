from app import db
from sqlalchemy.orm import relationship

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = relationship("Book", back_populates="author")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }