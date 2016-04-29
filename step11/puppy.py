import sys
from flask import Flask, jsonify, request, url_for
from models import db, Puppy
from schemas import ma, puppy_schema, puppies_schema
from slugify import slugify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppy.db"
db.init_app(app)
ma.init_app(app)

@app.route("/puppies/<int:id>")
def get_puppy(id):
    puppy = Puppy.query.get_or_404(id)
    return puppy_schema.jsonify(puppy)

@app.route("/puppies/", methods=["GET"])
def list_puppies():
    all_puppies = Puppy.query.all()
    return puppies_schema.jsonify(all_puppies)

@app.route("/puppies/", methods=["POST"])
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
    resp.headers["Location"] = puppy.url
    return resp

@app.route("/puppies/<int:id>", methods=["POST"])
def edit_puppy(id):
    puppy = Puppy.query.get_or_404(id)
    puppy, errors = puppy_schema.load(request.form, instance=puppy)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    puppy.slug = slugify(puppy.name)
    db.session.add(puppy)
    db.session.commit()

    resp = jsonify({"message": "updated"})
    return resp

@app.route("/puppies/<int:id>", methods=["DELETE"])
def delete_puppy(id):
    puppy = Puppy.query.get_or_404(id)
    db.session.delete(puppy)
    db.session.commit()
    return jsonify({"message": "deleted"})

@app.errorhandler(404)
def page_not_found(error):
    resp = jsonify({"error": "not found"})
    resp.status_code = 404
    return resp

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
