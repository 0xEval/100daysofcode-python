import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv('.env')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_sms_notification(self, flight_data):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        city_from = flight_data.city_from
        iata_from = flight_data.iata_from
        date_from = flight_data.date_from
        city_to = flight_data.city_to
        iata_to = flight_data.iata_to
        date_to = flight_data.date_to
        price = flight_data.lowest_price

        body = f"""
        Low price alert! Only {price}$ to fly from {city_from}-{iata_from} to {city_to}-{iata_to}, from {date_from} to {date_to}
    """

        client.messages.create(
            body=body,
            from_='+18584322788',
            to='+6596449397',
        )
