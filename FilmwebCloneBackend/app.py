from flask import Flask
from models import db
from blueprints import oauth, auth_blueprint
from dotenv import dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)
app.config["SECRET_KEY"] = 'very hard to guess key'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
oauth.init_app(app)

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
    
    app.register_blueprint(auth_blueprint)
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')