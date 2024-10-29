from __future__ import annotations

import numpy as np
from sklearn.cluster import AgglomerativeClustering

# TODO this could be a command line parameter
SEED = 123456
STOP_GROW_ODDS = 0.4

OPERATIONS = ["+", "-", "*", "/"]

MUTATION_PROBABILITY = 0.5
POPULATION_SIZE = 6
TOURNAMENT_SIZE = 2
ELITISM_SIZE = 1

EPSILON = 1e-5


rng = np.random.default_rng(SEED)

model = AgglomerativeClustering(metric="precomputed", linkage="average")
