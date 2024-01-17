from . import db
from .blueprints.artist import Artist
from .utils.utc_now import utcnow

class Director(db.Model, Artist):
  __tablename__ = 'director'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  def __init__(self, first_name, last_name, nationality, description, **kwargs):
    super(Director, self).__init__(**kwargs)
    self.first_name = first_name
    self.last_name = last_name
    self.nationality = nationality
    self.description = description