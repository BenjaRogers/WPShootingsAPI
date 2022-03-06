from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
##############################################################################
# Models
#############################################################################


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Person(db.Model):
    db_id = db.Column(db.Integer(), primary_key=True)
    id = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(50), nullable=True)
    date = db.Column(db.String(15), nullable=True)
    manner_of_death = db.Column(db.String(50), nullable=True)
    armed = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Float, nullable=True)
    gender = db.Column(db.String(5), nullable=True)
    race = db.Column(db.String(5), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    signs_of_mental_illness = db.Column(db.Boolean, nullable=True)
    threat_level = db.Column(db.String(50), nullable=True)
    flee = db.Column(db.String(50), nullable=True)
    body_camera = db.Column(db.Boolean, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    is_geocoding_exact = db.Column(db.Boolean, nullable=True)