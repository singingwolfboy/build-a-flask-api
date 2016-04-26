from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def get_puppy():
    puppy = {
        "name": "Rover",
        "image_url": "http://example.com/rover.jpg",
    }
    return jsonify(puppy)

if __name__ == "__main__":
    app.run(debug=True)
