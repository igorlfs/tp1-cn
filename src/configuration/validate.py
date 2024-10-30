from src.configuration import Configuration


def validate_config(config: Configuration) -> None:
    """Check if probabilities and sizes from config are valid."""
    validate_probaility(config["leaf_prob"], "Leaf")
    validate_probaility(config["mutation_prob"], "Mutation")

    validate_size(config["population_size"], "Population")
    validate_size(config["tournament_size"], "Tournament")

    # elitism_size can be zero (no elitism)


def validate_size(size: int, name: str) -> None:
    try:
        assert size > 0
    except AssertionError:
        print(f"{name} size must be greater than 0")
        raise ValueError from AssertionError


def validate_probaility(probability: float, name: str) -> None:
    try:
        assert probability >= 0 and probability <= 1
    except AssertionError:
        print(f"{name} probability must be a number between 0 and 1")
        raise ValueError from AssertionError
