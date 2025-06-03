import requests
from twilio.rest import Client

# ---------------- CONFIG ---------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"
TWILIO_PHONE = "+1234567890"
MY_PHONE = "+1098765432"

# ---------------- STOCK API ---------------- #
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

response = requests.get(stock_url, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = list(data.values())
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

# Calculate % difference
diff = yesterday_close - day_before_close
percent_change = round((diff / day_before_close) * 100, 2)
direction = "🔺" if diff > 0 else "🔻"

# ---------------- NEWS API ---------------- #
if abs(percent_change) > 5:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en"
    }

    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    # Format messages
    messages = [
        f"{STOCK}: {direction}{abs(percent_change)}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    # ---------------- SEND SMS ---------------- #
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for msg in messages:
        sms = client.messages.create(
            body=msg,
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(sms.status)
