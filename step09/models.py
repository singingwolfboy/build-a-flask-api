from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), nullable=False)
    thingy = db.Column(db.Boolean, nullable=False)
    image_url = db.Column(db.String(128), nullable=False)
