import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API = "TIME_SERIES_DAILY"
API_KEY_STOCK = "H69J2IC6891WO7LA"
API_KEY_NEWS = "e96d5a444fb74664b4e1e85fa96899ca"
URL_STOCK = "https://www.alphavantage.co/query"
URL_NEWS = "https://newsapi.org/v2/everything"

params_stock = {
    "function": API, 
    "symbol": STOCK, 
    "apikey": API_KEY_STOCK
}

params_news = {
    "apiKey": API_KEY_NEWS,
    "q": COMPANY_NAME,
    "to": str(datetime.now().date())
}

yesterday = datetime.now() - timedelta(days=1)
before_yesterday = datetime.now() - timedelta(days=2)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=URL_STOCK, params=params_stock)
response.raise_for_status()
data = response.json()
data_yesterday = float(data["Time Series (Daily)"][str(yesterday.date())]["4. close"])
data_before_yesterday = float(data["Time Series (Daily)"][str(before_yesterday.date())]["4. close"])

gap = data_yesterday - data_before_yesterday

ratio = gap / data_yesterday * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    response = requests.get(url=URL_NEWS, params=params_news)
    response.raise_for_status()
    data = response.json()["articles"]
    print(data[:3])

if ratio > 2:
    get_news()
elif ratio < -5:
    get_news()
else:
    print(f"Stock price move ${gap:.2f} or {ratio:.2f}%\n")
    get_news()


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

