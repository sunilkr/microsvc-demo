from flask import Flask,jsonify

API="library"

app = Flask(__name__)

@app.route("/api/library")
def index():
    return jsonify({'name':API})
