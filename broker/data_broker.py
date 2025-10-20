import time
from sources.nba_api_source import get_nba_api_data
from sources.espn_source import get_espn_data
from sources.balldontlie_source import get_balldontlie_data
from utils.normalization import normalize_snapshot
from utils.cache import save_cache

def fetch_latest_data():
    for fn in (get_nba_api_data, get_espn_data, get_balldontlie_data):
        try:
            data = fn()
            break
        except Exception:
            data = None
    if data is None:
        raise RuntimeError("All sources failed.")
    snapshot = normalize_snapshot(data)
    save_cache(snapshot)
    print("Snapshot updated", time.ctime())
    return snapshot
