import os
import re
import requests

from dotenv import load_dotenv
from typing import List
from twilio.rest import Client

COMPANY_NAME = 'Tesla Inc'
COMPANY_TICKER = 'TSLA'

load_dotenv('.env')
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
NEWSAPI_API_KEY = os.getenv('NEWSAPI_API_KEY')


def get_stock_daily(symbol: str) -> str:
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': ALPHAVANTAGE_API_KEY,
    }
    url = f'https://www.alphavantage.co/query'
    req = requests.get(url, params=parameters)
    data = req.json()
    daily_data = list(data['Time Series (Daily)'].values())[0]
    return daily_data


def get_difference_daily_percentage(data: str) -> float:
    price_open = float(data['1. open'])
    price_close = float(data['4. close'])
    return ((price_close - price_open) / price_open) * 100


def get_latest_news(company_name: str, date_range: str) -> List[str]:
    parameters = {
        'q': company_name,
        'from': date_range,
        'sortBy': 'popularity',
        'pageSize': 1,
        'apiKey': NEWSAPI_API_KEY,
    }
    url = 'https://newsapi.org/v2/everything'
    req = requests.get(url, params=parameters)
    data = req.json()
    return list(data['articles'])


def strip_html(s: str) -> str:
    """
    Strip HTML content from input parameter.
    This is used to remove HTML content from NewsAPI article description
    """
    txt = re.sub('<[^<]+?>.*?</[^<]+?>', '', s)   # Remove html tags
    return re.sub('\s+', ' ', txt)              # Normalize whitespace


def send_sms_notification():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    articles = get_latest_news(COMPANY_NAME, '2022-10-10')[0]
    # for article in articles:
    headline = articles['title']
    description = strip_html(articles['description'])

    daily_data = get_stock_daily(COMPANY_TICKER)
    daily_change = round(get_difference_daily_percentage(daily_data), 2)
    body_icon = '📈' if daily_change > 0 else '📉'
    body = f"""
{COMPANY_TICKER}: {body_icon}{abs(daily_change)}%\n
Headline: {headline}\n
Brief: {description}
"""

    client.messages.create(
        body=body,
        from_='+18584322788',
        to='+6596449397',
    )


data = get_stock_daily(COMPANY_TICKER)
price_diff = get_difference_daily_percentage(data)
if abs(price_diff) >= 1:
    send_sms_notification()
