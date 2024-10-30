from argparse import ArgumentParser

from src.configuration import Configuration
from src.configuration.validate import validate_config
from src.datasets import Datasets


def define_arguments(argument_parser: ArgumentParser) -> None:
    argument_parser.add_argument(
        "-s",
        "--seed",
        dest="seed",
        required=True,
        type=int,
        help="Seed to control randomness.",
    )
    argument_parser.add_argument(
        "-l",
        "--leaf-probability",
        dest="leaf_prob",
        required=True,
        type=float,
        help="Probability of generating a leaf when creating a random tree.",
    )
    argument_parser.add_argument(
        "-m",
        "--mutation-probability",
        dest="mutation_prob",
        required=True,
        type=float,
        help="Probability of mutating each node when traversing the tree.",
    )
    argument_parser.add_argument(
        "-r",
        "--reduction-probability",
        dest="reduction_prob",
        required=True,
        type=float,
        help="The probability of reducting an operator to a terminal (as opposed to swapping operators), when mutating nodes with operators.",
    )
    argument_parser.add_argument(
        "-p",
        "--population-size",
        dest="population_size",
        required=True,
        type=int,
        help="Number of individuals for each generation.",
    )
    argument_parser.add_argument(
        "-t",
        "--tournament-size",
        dest="tournament_size",
        required=True,
        type=int,
        help="Number of individuals when using per tournament when using tournament selection.",
    )
    argument_parser.add_argument(
        "-e",
        "--elitism-size",
        dest="elitism_size",
        required=True,
        type=int,
        help="Number of individuals to always select. If zero, there's no elitism.",
    )
    argument_parser.add_argument(
        "-g",
        "--max-generations",
        dest="max_generations",
        required=True,
        type=int,
        help="Maximum number of iterations.",
    )
    argument_parser.add_argument(
        "-d",
        "--max-depth",
        dest="max_depth",
        required=True,
        type=int,
        help="Maximum depth of tree.",
    )
    argument_parser.add_argument(
        dest="dataset",
        type=Datasets,
        help="Either 'breast_cancer_coimbra' or 'wine_red'",
    )


def load_config_from_args() -> Configuration:
    argument_parser = ArgumentParser()
    define_arguments(argument_parser)
    arguments = vars(argument_parser.parse_args())

    config = Configuration(**arguments)

    validate_config(config)

    return config
