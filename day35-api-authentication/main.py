import requests
import os
from twilio.rest import Client

API_URL = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'a3d70d5e144bf079fcfc5a0e89824b43'


def send_sms_notification() -> None:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.messages.create(
        body="It's going to rain today\nBring an Umbrella ☔️!",
        from_='+18584322788',
        to='+6596449397',
    )


def is_raining(weather_data) -> None:
    weather_slice = weather_data['list'][:4]   # Split in chunks of 3 hours
    for chunk_data in weather_slice:
        condition_code = chunk_data['weather'][0]['id']
        if condition_code < 700:
            send_sms_notification()
            break


parameters = {
    'lat': 1.290270,
    'lon': 103.851959,
    'appid': API_KEY,
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()

weather_data = response.json()
is_raining(weather_data)
