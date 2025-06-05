import smtplib
import datetime as dt
import random

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

# Get current day
now = dt.datetime.now()
weekday = now.weekday()

# Only send on Monday (0 = Monday, 6 = Sunday)
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="receiver@example.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
