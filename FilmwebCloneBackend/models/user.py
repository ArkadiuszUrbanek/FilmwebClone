from flask_login import UserMixin
from . import db
from enums import UserRole, UserAccountType
from .utils.utc_now import utcnow

class User(db.Model, UserMixin):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  first_name = db.Column(db.String(20), nullable = False)
  last_name = db.Column(db.String(40), nullable = False)
  email = db.Column(db.String(40), nullable = False)
  password_hash = db.Column(db.String(50), nullable = False)
  account_type = db.Column(db.Enum(UserAccountType), nullable = False)
  role = db.Column(db.Enum(UserRole), nullable = False)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  csrf_token_secret_key = None   

  forums = db.relationship('Forum', backref = 'user', lazy = True)
  messages = db.relationship('Message', backref = 'user', lazy = True, cascade = 'all, delete')
  reviews = db.relationship('Review', backref = 'user', lazy = True)

  def __init__(self, first_name, last_name, email, password_hash, account_type, role, **kwargs):
    super(User, self).__init__(**kwargs)
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password_hash = password_hash
    self.account_type = account_type
    self.role = role
