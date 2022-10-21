import os
import datetime
import requests

NOT_SO_SECRET_TOKEN = 'KnnJjoRXVzBm@X#Z#6y9'


def v1_create_user(username: str):
    params = {
        'token': NOT_SO_SECRET_TOKEN,
        'username': username,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }

    r = requests.post('https://pixe.la/v1/users', json=params)
    print(r.text)


def v1_post_graph_create(username: str, graph_id: str):
    url = f'https://pixe.la/v1/users/{username}/graphs'
    graph_params = {
        'id': username,
        'name': graph_id,
        'unit': 'Day(s)',
        'type': 'int',
        'color': 'shibafu',
    }
    headers = {'X-USER-TOKEN': NOT_SO_SECRET_TOKEN}

    r = requests.post(
        url,
        json=graph_params,
        headers=headers,
    )
    print(r.text)


def v1_post_graph_pixel(username: str, graph_id: str):
    url = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}'
    params = {
        'date': datetime.datetime.now().strftime('%Y%m%d'),
        'quantity': '1',
    }
    headers = {'X-USER-TOKEN': NOT_SO_SECRET_TOKEN}
    r = requests.post(url, json=params, headers=headers)
    print(r.text)


def v1_delete_graph_pixel(username: str, graph_id: str, date: str):
    url = f'https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}'
    headers = {'X-USER-TOKEN': NOT_SO_SECRET_TOKEN}
    r = requests.delete(url, headers=headers)
    print(r.text)


username = 'musangking'
graph_id = 'coding-graph'

now = datetime.datetime.now().strftime('%Y%m%d')

v1_post_graph_create(username, graph_id)
v1_post_graph_pixel(username, graph_id)
# v1_delete_graph_pixel(username, graph_id, now)
