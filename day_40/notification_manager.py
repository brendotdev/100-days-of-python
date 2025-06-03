import smtplib

MY_EMAIL = "youremail@example.com"
MY_PASSWORD = "yourpassword"

class NotificationManager:
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Flight Deal! ✈️\n\n{message}".encode("utf-8")
            )
