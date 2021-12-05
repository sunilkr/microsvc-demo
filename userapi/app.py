from flask import Flask,jsonify

API = "User"

app = Flask(__name__)

@app.route("/api/users")
def index():
    return jsonify({'name':API})
    