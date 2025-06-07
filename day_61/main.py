import smtplib
import datetime as dt
import random

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password_or_app_password"
TO_EMAIL = "recipient@example.com"

# Check if today is Monday
now = dt.datetime.now()
weekday = now.weekday()  # Monday = 0

if weekday == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
