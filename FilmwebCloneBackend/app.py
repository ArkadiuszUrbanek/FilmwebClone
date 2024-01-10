from flask import Flask
from flask_cors import CORS
from flask_session import Session
from models import db
from blueprints import oauth, auth_blueprint, bcrypt, login_manager, csrf, errors_blueprint, interceptors_blueprint, mail
from dotenv import dotenv_values
from ast import literal_eval

config = dotenv_values('.env')

app = Flask(__name__)

app.config['SECRET_KEY'] = config['APP_SECRET_KEY']
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_DOMAIN'] = '127.0.0.1'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = None
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['WTF_CSRF_SSL_STRICT'] = False
app.config['WTF_CSRF_METHODS'] = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'}
app.config['MAIL_SERVER'] = config['MAIL_SERVER']
app.config['MAIL_PORT'] = int(config['MAIL_PORT'])
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = literal_eval(config['MAIL_USE_TLS'])
app.config['MAIL_USE_SSL'] = literal_eval(config['MAIL_USE_SSL'])

db.init_app(app)
oauth.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)
mail.init_app(app)

Session(app)
CORS(app, resources = {
    r"/*": {
        'origins': ['http://localhost:5137'],
        'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
        'supports_credentials': True,
    }
})

with app.app_context():
    db.create_all()

app.register_blueprint(auth_blueprint)
app.register_blueprint(errors_blueprint)
app.register_blueprint(interceptors_blueprint)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')
