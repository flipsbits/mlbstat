BASE_URL = 'https://statsapi.mlb.com/api/'
V_1_0_URL = BASE_URL + 'v1/'
V_1_1_URL = BASE_URL + 'v1.1/'
SCHEDULE_URL = V_1_0_URL + 'schedule'
GAME_URL = V_1_1_URL + 'game/{}/feed/live'

# Default parameters

import requests
import datetime

def schedule(query_datetime=None,teamId=None):
    parameters = {'sportId': '1', 'language': 'en'}
    if query_datetime:
        parameters['date'] = datetime.date.today()
    if teamId:
        parameters['teamId'] = str(teamId)

    r = requests.get(SCHEDULE_URL, parameters)
    r.raise_for_status()
    return r.json()

def game(gameId):
    parameters = {'language': 'en'}
    r = requests.get(GAME_URL.format(gameId), parameters)
    r.raise_for_status()
    return r.json()
