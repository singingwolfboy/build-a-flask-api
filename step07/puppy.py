import sys
from flask import Flask, jsonify
from models import db, Puppy

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
