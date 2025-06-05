import requests
from bs4 import BeautifulSoup
import smtplib
import os

# Amazon product URL
URL = "https://www.amazon.com/dp/B09L5TRRMV"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Target price threshold
TARGET_PRICE = 150.00

# Your email credentials
EMAIL = os.environ.get("ALERT_EMAIL")
PASSWORD = os.environ.get("ALERT_PASS")

def check_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    
    price_tag = soup.find("span", class_="a-offscreen")
    if price_tag:
        price = float(price_tag.get_text().strip().replace("$", ""))
        title = soup.find(id="productTitle").get_text().strip()
        
        if price < TARGET_PRICE:
            send_email(title, price)
    else:
        print("Price not found.")

def send_email(title, price):
    message = f"{title} is now ${price}\n{URL}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
        print("Email sent!")

check_price()
