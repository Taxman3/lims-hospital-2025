
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.json
    contact = data.get("contact")
    message = data.get("message")
    return jsonify({"message": f"Notification sent to {contact}: {message}"})
