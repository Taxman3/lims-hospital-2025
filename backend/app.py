from flask import Flask, request, jsonify
import pandas as pd
from sqlalchemy import create_engine, text
from twilio.rest import Client

app = Flask(__name__)

# Cloud Database Connection (MySQL)
engine = create_engine('mysql://username:password@your-cloud-sql-db')

# Twilio client setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Function to send inventory notification
def send_inventory_alert(item_name):
    message = client.messages.create(
        body=f"Inventory low for {item_name}. Please restock.",
        from_='+1234567890',  # Your Twilio phone number
        to='+0987654321'  # Your target phone number
    )
    print(f"Alert sent: {message.sid}")

# Function to check inventory levels
def check_inventory():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT item_name, quantity FROM inventory"))
        for row in result:
            item_name = row['item_name']
            quantity = row['quantity']
            if quantity < 5:  # Example threshold level
                send_inventory_alert(item_name)

# Endpoint to manually trigger inventory check (for testing)
@app.route('/check-inventory', methods=['GET'])
def manual_inventory_check():
    check_inventory()
    return jsonify({"message": "Inventory check completed."})

# Endpoint for drag-and-drop file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_excel(file)
    # Process and save data to DB
    df.to_sql('patients', con=engine, if_exists='append', index=False)
    return jsonify({"message": "Data uploaded successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
