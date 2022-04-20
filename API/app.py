from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import API.project_secrets as ps
from API.models import db

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = ps.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = ps.db_uri_production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# migrate = Migrate(app, db)
