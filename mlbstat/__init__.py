BASE_URL = 'https://statsapi.mlb.com/api/'
V_1_0_URL = BASE_URL + 'v1/'
V_1_1_URL = BASE_URL + 'v1.1/'
SCHEDULE_URL = V_1_0_URL + 'schedule'
GAME_URL = V_1_1_URL + 'game/{}/feed/live'

# Default parameters

import requests
import datetime

'''
Get the schedule for the given day and team.  By default, the day will be today
and games for all teams will be returned.

If a connection can not be established, such as due to a network or DNS
outage, a ValueError will be raised.
'''
def schedule(day=None,teamId=None):
    parameters = {'sportId': '1', 'language': 'en'}
    if day:
        parameters['date'] = str(day)
    if teamId:
        parameters['teamId'] = str(teamId)

    try:
        r = requests.get(SCHEDULE_URL, parameters)
    except ConnectionError:
        raise ValueError('Failed to retrieve MLB schedule information.')
    r.raise_for_status()
    return r.json()

'''
Get information about a game.

If a connection can not be established, such as due to a network or DNS
outage, a ValueError will be raised.
'''
def game(gameId):
    parameters = {'language': 'en'}
    try:
        r = requests.get(GAME_URL.format(gameId), parameters)
    except ConnectionError:
        raise ValueError('Failed to retrieve MLB game information.')
    r.raise_for_status()
    return r.json()
