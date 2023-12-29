from . import db
from .movie_director import movie_director
from .utils.artist import Artist

class Director(db.Model, Artist):
  movies = db.relationship("Movie", secondary=movie_director, back_populates="directors")