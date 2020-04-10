from flask import jsonify
import json

def api_json(data):
    """Takes JSON data and proceeds to turn it into a flask jsonify object"""
    data = jsonify(data)

    return json.dumps({"status": data.status,
        "mimetype": data.mimetype,
        "data": data.json}, indent=4)