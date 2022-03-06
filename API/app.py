from flask import Flask
from ... ApiShoot import project_secrets as ps
from models import db, User, Person

app = Flask(__name__)

app.config['SECRET_KEY'] = ps.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = ps.db_uri
db.init_app(app)
