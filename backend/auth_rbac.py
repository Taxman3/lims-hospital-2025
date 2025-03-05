
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Simulated database of users with roles
users_db = {
    "admin": {"password": "adminpass", "role": "admin"},
    "doctor": {"password": "doctorpass", "role": "doctor"},
    "pharmacist": {"password": "pharmacistpass", "role": "pharmacist"},
    "receptionist": {"password": "receptionistpass", "role": "receptionist"}
}

def generate_token(username, role):
    token = jwt.encode({'user': username, 'role': role, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'], algorithm="HS256")
    return token

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users_db and users_db[username]["password"] == password:
        token = generate_token(username, users_db[username]["role"])
        return jsonify({"token": token, "role": users_db[username]["role"]})
    
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing!"}), 401

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": f"Access granted to {data['user']} with role {data['role']}"})
    except:
        return jsonify({"message": "Token is invalid!"}), 401

if __name__ == "__main__":
    app.run(debug=True)
