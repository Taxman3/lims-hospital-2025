
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    stats = {
        "total_patients": random.randint(100, 500),
        "total_tests": random.randint(500, 2000),
        "medicines_low_stock": random.randint(5, 50)
    }
    return jsonify(stats)
