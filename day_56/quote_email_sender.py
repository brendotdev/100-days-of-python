import smtplib
import datetime as dt
import random

# Email credentials
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

# Get the current day
now = dt.datetime.now()
weekday = now.weekday()  # Monday = 0, Sunday = 6

if weekday == 0:  # Send motivational email on Mondays
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="recipient_email@example.com",
            msg=f"Subject:Monday Motivation 💪\n\n{quote}"
        )
