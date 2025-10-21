import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json, time
from sources.espn_source import get_espn_data
from sources.nba_api_source import get_nba_api_data
from sources.balldontlie_source import get_balldontlie_data
from utils.normalization import normalize_snapshot
from utils.cache import save_cache


def fetch_latest_data():
    try:
        data = get_nba_api_data()
    except Exception:
        try:
            data = get_espn_data()
        except Exception:
            data = get_balldontlie_data()

    snapshot = normalize_snapshot(data)
    save_cache(snapshot)
    print("Snapshot updated", time.ctime())
    return snapshot
