import requests
import os
import dotenv


dotenv.load_dotenv('.env')
TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = 'https://api.tequila.kiwi.com'
        self.headers = {
            'apikey': TEQUILA_API_KEY,
            'accept': 'application/json',
        }

    def get_iata_from_name(self, city_name):
        """Returns IATA code corresponding to `city_name` passed in parameter"""
        url = f'{self.endpoint}/locations/query'
        params = {
            'term': city_name,
            'locale': 'en-US',
            'location_types': 'city',
        }
        response = requests.get(url, params=params, headers=self.headers)
        results = response.json()['locations']
        code = results[0]['code']
        return code

    # Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
    def get_lowest_price_between_range(
        self, fly_from, fly_to, date_from, date_to
    ):
        """Returns latest lowest price corresponding to `iata_code` passed in parameter"""
        url = f'{self.endpoint}/v2/search'
        params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to,
            'curr': 'USD',
            'sort': 'price',
            'limit': 1,
        }
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()['data'][0]['price']

    # ... implement more API interfaces ...
