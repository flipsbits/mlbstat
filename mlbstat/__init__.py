BASE_URL = 'https://statsapi.mlb.com/api/'
V_1_0_URL = BASE_URL + 'v1/'
V_1_1_URL = BASE_URL + 'v1.1/'
SCHEDULE_URL = V_1_0_URL + 'schedule?sportId=1&date={}&language=en'
GAME_URL = V_1_1_URL + 'game/{}/feed/live?language=en'

import requests
import datetime

def schedule(query_datetime=None):
    if not query_datetime:
        query_datetime = datetime.date.today()
    r = requests.get(SCHEDULE_URL.format(query_datetime))
    r.raise_for_status()
    return r.json()

def game(gameId):
    r = requests.get(GAME_URL.format(gameId))
    r.raise_for_status()
    return r.json()
