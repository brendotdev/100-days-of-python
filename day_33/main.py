import requests
from datetime import datetime
import smtplib
import time

# ------------------ YOUR LOCATION ------------------ #
MY_LAT = 37.7749     # Example: San Francisco latitude
MY_LONG = -122.4194  # Example: San Francisco longitude

# ------------------ EMAIL INFO ------------------ #
MY_EMAIL = "youremail@example.com"
MY_PASSWORD = "yourpassword"

# ------------------ CHECK FUNCTIONS ------------------ #

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_long <= MY_LONG + 5
    )

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.utcnow().hour

    return now >= sunset or now <= sunrise

# ------------------ LOOP ------------------ #
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up! 👀\n\nThe ISS is overhead. Go look up!"
            )
