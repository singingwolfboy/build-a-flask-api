import sys
from flask import Flask, jsonify, request, url_for
from models import db, Puppy
from schemas import ma, puppy_schema
from slugify import slugify


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppy.db"
db.init_app(app)
ma.init_app(app)


@app.route("/<slug>")
def get_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    return puppy_schema.jsonify(puppy)


@app.route("/", methods=["POST"])
def create_puppy():
    puppy, errors = puppy_schema.load(request.form)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    puppy.slug = slugify(puppy.name)
    db.session.add(puppy)
    db.session.commit()

    resp = jsonify({"message": "created"})
    resp.status_code = 201
    location = url_for("get_puppy", slug=puppy.slug)
    resp.headers["Location"] = location
    return resp


@app.route("/<slug>", methods=["POST"])
def edit_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    puppy, errors = puppy_schema.load(request.form, instance=puppy)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    puppy.slug = slugify(puppy.name)
    db.session.add(puppy)
    db.session.commit()

    resp = jsonify({"message": "updated"})
    location = url_for("get_puppy", slug=puppy.slug)
    resp.headers["Location"] = location
    return resp


@app.route("/<slug>", methods=["DELETE"])
def delete_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    db.session.delete(puppy)
    db.session.commit()
    return jsonify({"message": "deleted"})


if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")

    elif "seeddb" in sys.argv:
        with app.app_context():
            p1 = Puppy(slug="rover", name="Rover",
                       image_url="http://example.com/rover.jpg")
            db.session.add(p1)
            p2 = Puppy(slug="spot", name="Spot",
                       image_url="http://example.com/spot.jpg")
            db.session.add(p2)
            db.session.commit()
        print("Database seeded!")

    else:
        app.run(debug=True)
