################################################################################
#                                   data.py                                    #
#                                                                              #
# Description:                                                                 #
#  Generate Quizzler content from Opentrivia db                                #
################################################################################

import requests

################################################################################
#                                  CONSTANTS                                   #
################################################################################

URL = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,  # amount of Qs per batch
    'category': 18,
    'type': 'boolean',
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()

question_data = data['results']
