from flask import Flask,jsonify

API="books"

app = Flask(__name__)

@app.route("/api/books")
def index():
    return jsonify({'name':API})
