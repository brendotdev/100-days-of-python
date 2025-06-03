import requests
from twilio.rest import Client

# ---------------- CONFIG ---------------- #
OWM_API_KEY = "your_openweather_api_key"
LAT = 37.7749  # Example: San Francisco
LON = -122.4194
TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
MY_PHONE = "+1098765432"

# ---------------- API REQUEST ---------------- #
weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()

# ---------------- CHECK FOR RAIN ---------------- #
will_rain = False
for hour_data in weather_data["hourly"][:12]:  # Check next 12 hours
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

# ---------------- SEND SMS ---------------- #
if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="☔ Heads up! It's going to rain. Bring an umbrella!",
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
    print(message.status)
