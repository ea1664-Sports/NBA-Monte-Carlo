import json
def save_cache(snapshot, path="latest_snapshot.json"):
    with open(path,"w") as f:
        json.dump(snapshot,f)
