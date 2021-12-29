from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/taxidata"
mongo = PyMongo(app)
collection  = mongo.db.nyctaxidata

collection.create_index('total_amount')


@app.route("/", methods=['GET'])
def Index():
    try:
        return jsonify(
        data='Welcome to APP refer to APIs to get data' ,
        status=200
        )   
    except Exception as ex:
        return jsonify(ex), 400
    

@app.route("/api/<amount>", methods=['GET'])
def Trips(amount):
    try:
        trip_data = collection.find({"total_amount": { "$gt": float(amount)}})
        # cursor clone is used as it doesn't consume cursor
        if len(list(trip_data.clone())) > 0:
            return dumps({'Amount' :  amount,
                          'Trips_Count':len(list(trip_data.clone()))})

        return jsonify(
        data='No data Found' ,
        status=400
        )   
    except Exception as ex:
        return jsonify(ex), 400

if __name__=='__main__':
    app.run(host='localhost', port=8000, debug=False)