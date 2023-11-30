
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
        response = requests.get("https://api.ipify.org/?format=json")
        data = json.loads(response.text)
        ip_address = data['ip']
        print(ip_address)
        # https://ipwhois.app/json/20.235.87.227
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

    print(f'Received Geolocation Data - Latitude: {latitude}, Longitude: {longitude}')
    
    return 'Geolocation data received on the server!'

if __name__ == '__main__':
    app.run(debug=True)

