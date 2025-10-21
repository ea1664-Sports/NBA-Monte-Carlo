import random, statistics
def run_simulation(snapshot, iters=10000):
    scores = [random.gauss(110,10) - random.gauss(108,10) for _ in range(iters)]
    return {"mean_margin": statistics.mean(scores),
            "stddev": statistics.stdev(scores),
            "iterations": iters}
