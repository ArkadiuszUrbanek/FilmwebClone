from .. import db

class Artist():
  first_name = db.Column(db.String(20), nullable = False)
  last_name = db.Column(db.String(40), nullable = False)
  nationality = db.Column(db.String(70), nullable = True)
  description = db.Column(db.String(1000), nullable = True)