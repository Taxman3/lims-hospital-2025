
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-invoice', methods=['POST'])
def generate_invoice():
    data = request.json
    patient = data.get("patient_name")
    amount = data.get("amount")
    return jsonify({"message": f"Invoice generated for {patient}: ${amount}"})
