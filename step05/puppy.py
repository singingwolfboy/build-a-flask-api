from flask import Flask, jsonify, abort
app = Flask(__name__)

PUPPIES = [
    {
        "name": "Rover",
        "image_url": "http://example.com/rover.jpg",
    },
    {
        "name": "Spot",
        "image_url": "http://example.com/spot.jpg",
    },
]

@app.route("/<int:index>")
def get_puppy(index):
    try:
        puppy = PUPPIES[index]
    except IndexError:
        abort(404)
    return jsonify(puppy)

if __name__ == "__main__":
    app.run(debug=True)
