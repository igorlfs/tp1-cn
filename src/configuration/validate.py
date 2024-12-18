from src.configuration import Configuration


def validate_config(config: Configuration) -> None:
    """Check if probabilities and sizes from config are valid."""
    validate_probaility(config["leaf_prob"], "Leaf")
    validate_probaility(config["mutation_prob"], "Mutation")
    validate_probaility(config["swap_terminal_prob"], "Swap Terminal")
    validate_probaility(config["swap_operator_prob"], "Swap Operator")
    validate_probaility(config["crossover_prob"], "Crossover")

    validate_size(config["population_size"], "Population size must be greater than 0")
    validate_size(config["tournament_size"], "Tournament size must be greater than 0")

    # elitism_size can be zero (no elitism)
    validate_size(config["tournament_size"], "Tournament size must be 0 or greater", -1)

    try:
        assert config["elitism_size"] < config["population_size"]
    except AssertionError:
        print("Elitism size must be less than population size")
        raise ValueError from AssertionError

    try:
        assert config["tournament_size"] < config["population_size"]
    except AssertionError:
        print("Tournament size must less than population size")
        raise ValueError from AssertionError

    validate_size(config["tournament_size"], "Tournament size must be at least 1")

    validate_size(config["max_generations"], "There must at least 1 generation")
    validate_size(config["max_depth"], "Max depth must be greater than 0")


def validate_size(size: int, message: str, floor: int = 0) -> None:
    try:
        assert size > floor
    except AssertionError:
        print(message)
        raise ValueError from AssertionError


def validate_probaility(probability: float, name: str) -> None:
    try:
        assert probability >= 0 and probability <= 1
    except AssertionError:
        print(f"{name} probability must be a number between 0 and 1")
        raise ValueError from AssertionError
