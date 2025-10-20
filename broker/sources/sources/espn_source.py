import requests
def get_espn_data():
    r = requests.get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams")
    r.raise_for_status()
    teams = [t["team"] for t in r.json()["sports"][0]["leagues"][0]["teams"]]
    return teams
