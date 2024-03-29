from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .anonymous_user import AnonymousUser
from .actor import Actor
from .director import Director
from .forum import Forum
from .genre import Genre
from .message import Message
from .movie import Movie
from .review import Review
from .salt import Salt