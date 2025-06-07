import requests
from twilio.rest import Client

# OpenWeatherMap API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "your_openweathermap_api_key"

# Twilio credentials
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
MY_PHONE = "+0987654321"

weather_params = {
    "lat": 38.5816,  # Example: Sacramento, CA
    "lon": -121.4944,
    "appid": API_KEY,
    "cnt": 4,  # next 12 hours (3-hour intervals)
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today ☔️. Bring an umbrella!",
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
    print(message.status)
