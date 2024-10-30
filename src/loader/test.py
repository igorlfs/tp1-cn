import os

from dotenv import load_dotenv

from src.configuration import Configuration
from src.configuration.validate import validate_config
from src.datasets import Datasets


def load_test_config() -> Configuration:
    """Read a default Configuration from the .env.test file."""
    load_dotenv(".env.test")

    config = Configuration(
        {
            "seed": int(os.environ["SEED"]),
            "leaf_prob": float(os.environ["LEAF_PROBABILITY"]),
            "mutation_prob": float(os.environ["MUTATION_PROBABILITY"]),
            "population_size": int(os.environ["POPULATION_SIZE"]),
            "tournament_size": int(os.environ["TOURNAMENT_SIZE"]),
            "elitism_size": int(os.environ["ELITISM_SIZE"]),
            "max_generations": int(os.environ["MAX_GENERATIONS"]),
            "max_depth": int(os.environ["MAX_DEPTH"]),
            "dataset": Datasets(os.environ["DATASET"]),
        }
    )

    # Important to not mess up the .env.test file
    validate_config(config)

    return config
