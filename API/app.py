from flask import Flask
from flask_migrate import Migrate
import project_secrets as ps
from models import db

app = Flask(__name__)

app.config['SECRET_KEY'] = ps.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = ps.db_uri_production
db.init_app(app)
# migrate = Migrate(app, db)
