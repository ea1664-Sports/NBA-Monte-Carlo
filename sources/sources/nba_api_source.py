from nba_api.stats.endpoints import leaguedashteamstats

def get_nba_api_data():
    stats = leaguedashteamstats.LeagueDashTeamStats().get_data_frames()[0]
    return stats.to_dict(orient="records")
