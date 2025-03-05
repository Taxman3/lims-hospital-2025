
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def generate_token(username):
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'], algorithm="HS256")
    return token

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username == "admin" and password == "password":  # Replace with database check
        token = generate_token(username)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
