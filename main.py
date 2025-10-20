from broker.data_broker import fetch_latest_data
from engine.montecarlo import run_simulation
from engine.audit import audit_results

def main():
    snapshot = fetch_latest_data()
    sim_output = run_simulation(snapshot)
    audit_results(sim_output)

if __name__ == "__main__":
    main()
