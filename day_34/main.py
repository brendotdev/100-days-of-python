import datetime as dt
import pandas
import random
import smtplib

# ------------------ YOUR EMAIL INFO ------------------ #
MY_EMAIL = "youremail@example.com"
MY_PASSWORD = "yourpassword"

# ------------------ GET TODAY ------------------ #
today = (dt.datetime.now().month, dt.datetime.now().day)

# ------------------ READ BIRTHDAYS ------------------ #
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# ------------------ CHECK & SEND ------------------ #
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # Choose random letter template
    template_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(template_path) as letter_file:
        contents = letter_file.read()
        personalized_letter = contents.replace("[NAME]", name)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )
