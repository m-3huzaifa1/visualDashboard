from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config["MONGO_URI"] = "mongodb+srv://m3huzaifa1:Huzaifa123@m3huzaifa1.uwkb6rb.mongodb.net/visualDashboard"
mongo = PyMongo(app)

@app.route("/api", methods=['GET', 'POST'])
def get_server():
    return "Server Running"

@app.route("/api/data", methods=['GET', 'POST'])
def get_data():
    data = mongo.db.visualdb.find()
    return json_util.dumps(data)

@app.route("/api/data/filter", methods=["POST"])
def filter_data():
    filters = request.get_json()
    data = mongo.db.visualdb.find(filters)
    return json_util.dumps(data)

@app.route("/api/insert_data", methods=["POST"])
def insert_data():
    data = request.get_json()
    mongo.db.visualdb.insert_many(data)
    return jsonify({"message": "Data inserted successfully"})

if __name__ == "__main__":
    app.run(debug = True, port=8888, host='127.0.0.1')
