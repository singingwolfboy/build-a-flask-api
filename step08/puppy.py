import sys
from flask import Flask, jsonify, request, url_for
from models import db, Puppy
from slugify import slugify


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppy.db"
db.init_app(app)


@app.route("/<slug>")
def get_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    output = {
        "name": puppy.name,
        "image_url": puppy.image_url,
    }
    return jsonify(output)


@app.route("/", methods=["POST"])
def create_puppy():
    # validate attributes
    name = request.form.get("name")
    if not name:
        return "name required", 400
    image_url = request.form.get("image_url")
    if not image_url:
        return "image_url required", 400
    slug = slugify(name)

    # create in database
    puppy = Puppy(slug=slug, name=name,
                  image_url=image_url)
    db.session.add(puppy)
    db.session.commit()

    # return HTTP response
    location = url_for("get_puppy", slug=slug)
    resp = jsonify({"message": "created"})
    resp.status_code = 201
    resp.headers["Location"] = location
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
