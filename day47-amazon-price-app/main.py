import os
import dotenv
import requests
import smtplib
import email.message

from bs4 import BeautifulSoup

dotenv.load_dotenv('.env')

# Amazon Zojirushi Rice Cooker!!!
URL = 'https://www.amazon.com/dp/B00007J5U7/ref=sbl_dpx_kitchen-electric-cookware_B007WQ9YNO_0'
TARGET_PRICE = 300.99
MAILTRAP_CLIENT = os.getenv('MAILTRAP_CLIENT')
MAILTRAP_SECRET = os.getenv('MAILTRAP_SECRET')


def send_mail(body) -> None:
    # Use Python built-in email class to avoid formatting issues
    sender = 'Bob <bob@localhost.home>'
    m = email.message.Message()
    m['From'] = sender
    m['To'] = sender   # self-sent
    m['Subject'] = 'Item has reached target price!'
    m.set_payload(body)

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.starttls()
        server.login(MAILTRAP_CLIENT, MAILTRAP_SECRET)
        server.sendmail(sender, sender, m.as_string())


def extract_price_data(item_url: str) -> float:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    }

    response = requests.get(URL, headers=headers)
    data = response.text

    soup = BeautifulSoup(data, 'lxml')
    price_div = soup.find('div', id='corePrice_feature_div')
    price_s = price_div.find('span', class_='a-offscreen').getText()
    price = float(price_s.split('$')[1])

    return price


def main():

    item_price = extract_price_data(URL)

    if item_price <= TARGET_PRICE:
        body = f'The Zoji is under my target price of ${TARGET_PRICE}, you can get it for ${item_price} on Amazon!\n{URL}'
        send_mail(body)


if __name__ == '__main__':
    main()
