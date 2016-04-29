from flask import Flask, jsonify, abort
app = Flask(__name__)


PUPPIES = {
    "rover": {
        "name": "Rover",
        "image_url": "http://example.com/rover.jpg",
    },
    "spot": {
        "name": "Spot",
        "image_url": "http://example.com/spot.jpg",
    },
}


@app.route("/<slug>")
def get_puppy(slug):
    try:
        puppy = PUPPIES[slug]
    except KeyError:
        abort(404)
    return jsonify(puppy)


if __name__ == "__main__":
    app.run(debug=True)
