import requests
import jwt
import datetime
import os

################################################################################
#                                  CONSTANTS                                   #
################################################################################

GENDER = 'male'
WEIGHT_KG = 100
HEIGHT_CM = 200
AGE = 42

APP_ID = os.getenv('NT_APP_ID')
APP_KEY = os.getenv('NT_APP_KEY')

################################################################################
#                                  FUNCTIONS                                   #
################################################################################


def sheety_save_data_to_row(data: str):
    url = 'https://api.sheety.co/3d25f658aa1c388eeeb613343ffa7c48/copyOfMyWorkouts/workouts'
    now = datetime.datetime.now()
    params = {
        'workout': {
            'date': now.strftime('%d/%m/%Y'),
            'time': now.strftime('%H:%M:%S'),
            'exercise': data['name'].title(),
            'duration': data['duration_min'],
            'calories': data['nf_calories'],
        }
    }
    headers['Content-type'] = 'application/json'

    req = requests.post(url, json=params, headers=headers)
    print(req.json())


def post_v2_natural_exercise(query: str):
    url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    params = {
        'query': query,
        'gender': GENDER,
        'weight_kg': WEIGHT_KG,
        'height_cm': HEIGHT_CM,
        'age': AGE,
    }

    req = requests.post(url, json=params, headers=headers)
    data = req.json()
    return data


################################################################################
#                                     MAIN                                     #
################################################################################

user_input = input('What did you do today? ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Authorization': f'Bearer {os.getenv("TOKEN")}',
}

result = post_v2_natural_exercise(user_input)
for exercise in result['exercises']:
    sheety_save_data_to_row(exercise)
