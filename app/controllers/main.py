from flask import jsonify


def home():
    return jsonify({'message': 'Flask API'}), 200
