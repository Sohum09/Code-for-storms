import requests

# Define the API endpoint URL
url = 'https://weatherunion.com/gw/weather/external/v0/get_locality_weather_data'

# Define the headers with the required content-type and your API key
headers = {
    'content-type': 'application/json',
    'x-zomato-api-key': '0b96804b60bf26c471255275a86f4d6e'
}

# Define the parameters (locality_id)
params = {
    'locality_id': 'ZWL001334'
}

# Make a GET request to the API
response = requests.get(url, headers=headers, params=params)
result = ""
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract relevant information from the response
    status = data['status']
    message = data['message']
    device_type = data['device_type']
    locality_weather_data = data['locality_weather_data']
    
    # Print the extracted information
    result += (f"Status: {status}")
    result += (f"Message: {message}")
    result += (f"Device Type: {device_type}")
    result += ("Locality Weather Data:")
    result += (f"  Temperature: {locality_weather_data['temperature']} °C")
    result += (f"  Humidity: {locality_weather_data['humidity']} %")
    result += (f"  Wind Speed: {locality_weather_data['wind_speed']} m/s")
    result += (f"  Wind Direction: {locality_weather_data['wind_direction']} degrees")
    result += (f"  Rain Intensity: {locality_weather_data['rain_intensity']} mm/min")
    result += (f"  Rain Accumulation: {locality_weather_data['rain_accumulation']} mm")
else:
    result = (f"Error: {response.status_code} - {response.reason}")
