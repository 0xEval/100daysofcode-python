import requests
import os
import dotenv

from flight_data import FlightData


dotenv.load_dotenv('.env')
SHEETY_APP_ID = os.getenv('SHEETY_APP_ID')
SHEETY_API_KEY = os.getenv('SHEETY_API_KEY')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, project_name, sheet_id, sheet_name) -> None:
        self.project_name = project_name
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        self.url = f'https://api.sheety.co/{self.sheet_id}/{self.project_name}/{self.sheet_name}'

    def get_rows(self):
        req = requests.get(self.url)
        return req.json()

    def add_row(self, city, code, price):
        params = {
            'price': {
                'city': city,
                'iataCode': code,
                'lowestPrice': price,
            }
        }
        print(params)
        headers = {'Content-Type': 'application/json'}
        req = requests.post(self.url, json=params, headers=headers)
        print(req.json())
        return req.json()

    def edit_row(self, row_id, **kwargs):
        url = f'{self.url}/{row_id}'
        params = {'price': {**kwargs}}
        headers = {'Content-Type': 'application/json'}
        req = requests.put(url, json=params, headers=headers)
        return req.json()

    def delete_row(self):
        pass
