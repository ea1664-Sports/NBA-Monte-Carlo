import json, time
def audit_results(result):
    with open("audit_log.json","a") as f:
        f.write(json.dumps({"timestamp":time.time(),"result":result})+"\n")
    print("Audit logged.")
