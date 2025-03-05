
import requests

# Test if backend is running
try:
    response = requests.get("http://localhost:5000/healthcheck")
    if response.status_code == 200:
        print("✅ Backend is running successfully.")
    else:
        print("❌ Backend returned an error.")
except:
    print("❌ Backend is not responding.")

# Test if frontend is accessible
try:
    response = requests.get("http://localhost:3000")
    if response.status_code == 200:
        print("✅ Frontend is running successfully.")
    else:
        print("❌ Frontend returned an error.")
except:
    print("❌ Frontend is not responding.")
