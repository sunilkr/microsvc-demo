from flask import Flask,jsonify

API="Shope"

app = Flask(__name__)

@app.route("/api/order")
def index():
    return jsonify({'name':API})
    