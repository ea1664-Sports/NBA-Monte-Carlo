import requests

def get_espn_data():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    teams = [t["team"] for t in r.json()["sports"][0]["leagues"][0]["teams"]]
    return teams
