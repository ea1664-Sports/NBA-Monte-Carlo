import requests

def get_nba_api_data():
    r = requests.get("https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json", timeout=20)
    r.raise_for_status()
    return r.json()
