import datetime as dt
import pandas
import random
import smtplib

# Email credentials
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

# Get today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Load birthday data
data = pandas.read_csv("birthdays.csv")

# Create dictionary from birthday data
birthday_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}

# If today matches a birthday, send email
if today in birthday_dict:
    person = birthday_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday! 🎉\n\n{content}"
        )
