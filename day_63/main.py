import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/dp/B0949CV7T3"  # Replace with your desired product
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")

# Get the product price
price_tag = soup.find(name="span", class_="a-offscreen")
title_tag = soup.find(id="productTitle")

if price_tag and title_tag:
    price = price_tag.get_text()
    title = title_tag.get_text().strip()
    print(f"Product: {title}")
    print(f"Price: {price}")
else:
    print("Failed to retrieve product price or title.")
