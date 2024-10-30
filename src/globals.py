import random

import numpy as np

from src.loader import config

rng = np.random.default_rng(config["seed"])

random.seed(config["seed"])
