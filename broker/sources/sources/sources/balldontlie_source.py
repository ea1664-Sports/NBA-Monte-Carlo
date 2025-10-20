import requests
def get_balldontlie_data():
    r = requests.get("https://www.balldontlie.io/api/v1/teams")
    r.raise_for_status()
    return r.json()["data"]
