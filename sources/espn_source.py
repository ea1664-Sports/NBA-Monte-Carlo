import requests

def get_espn_data():
    r = requests.get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams", timeout=20)
    r.raise_for_status()
    return r.json()
