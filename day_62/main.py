import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_app_password"

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays from CSV
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# If today matches a birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        contents = letter_file.read()
        personalized_letter = contents.replace("[NAME]", birthday_person["name"])

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )
