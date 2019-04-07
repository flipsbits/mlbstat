BASE_URL = 'https://statsapi.mlb.com/api/'
V_1_0_URL = BASE_URL + 'v1/'
V_1_1_URL = BASE_URL + 'v1.1/'
SCHEDULE_URL = V_1_0_URL + 'schedule'
LEADERS_URL = V_1_0_URL + 'stats/leaders'
GAME_URL = V_1_1_URL + 'game/{}/feed/live'

import requests
import datetime

'''
Get the schedule for the given day and team.  By default, the day will be today
and games for all teams will be returned.

If a connection can not be established, such as due to a network or DNS
outage, a ValueError will be raised.
'''
SCHEDULE_DEFAULT_PARAMS = {
  'sportId': '1',
  'date': str(datetime.date.today()),
  # R is Regular season, E is exhibition, S is Spring Training
  'gameTypes': 'R',
  'hydrate': 'team,linescore,flags,liveLookin,review,\
      game(content(summary,media(epg)),tickets),seriesStatus(useOverride=true),\
      broadcasts(all)',
  'useLatestGames': 'false',
  'language': 'en',
  # 103 is AL, 104 is NL
  'leagueId': '103,104'
}
def schedule(parameters=SCHEDULE_DEFAULT_PARAMS):
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
GAME_FEED_DEFAULT_PARAMS = {
  'language': 'en'
}
def gameFeed(gameId, parameters=GAME_FEED_DEFAULT_PARAMS):
    parameters = {'language': 'en'}
    try:
        r = requests.get(GAME_URL.format(gameId), parameters)
    except ConnectionError:
        raise ValueError('Failed to retrieve MLB game information.')
    r.raise_for_status()
    return r.json()

'''
Get information about statistical league leaders.

If a connection can not be established, such as due to a network or DNS
outage, a ValueError will be raised.
'''
LEADERS_DEFAULT_PARAMS = {
  'leaderCategories': 'wins,saves,earnedRunAverage,strikeouts,battingAverage,runs, \
  homeRuns,runsBattedIn,stolenBases',
  # R is Regular season, E is exhibition, S is Spring Training
  'leaderGameTypes': 'R',
  'season': datetime.date.today().year,
  'hydrate': 'person,team',
  'limit': '1'
}
def leaders(parameters=LEADERS_DEFAULT_PARAMS):
    try:
        r = requests.get(LEADERS_URL, parameters)
    except ConnectionError:
        raise ValueError('Failed to retrieve MLB game information.')
    r.raise_for_status()
    return r.json()

'''
TODO

Seasons
https://statsapi.mlb.com/api/v1/seasons?season=2019&season=2018&season=2017&season=2016&season=2015&sportId=1

Game Content
https://statsapi.mlb.com/api/v1/game/564834/content?language=en

People
https://statsapi.mlb.com/api/v1/people?personIds=643217&personIds=519443&personIds=518489&personIds=624407&personIds=605155&personIds=605141&personIds=456665&personIds=519048&personIds=593428&personIds=646240&personIds=456488&personIds=598265&personIds=543877&personIds=456034&personIds=502110&season=2019&hydrate=stats(group=hitting,type=season,season=2019,gameType=R)
'''
