from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class Configuration:
    path: str
    name: str
    iter: int
    var: int


def load_config_from_args() -> Configuration:
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        "-p",
        "--path",
        dest="path",
        required=True,
        type=str,
        help="Path to folder containing dumped execution data.",
    )
    argument_parser.add_argument(
        "-n",
        "--name",
        dest="name",
        required=True,
        type=str,
        help="Base filename for dumps.",
    )
    argument_parser.add_argument(
        "-i",
        "--iter",
        dest="iter",
        required=True,
        type=int,
        help="Number of iterations to analyze.",
    )
    argument_parser.add_argument(
        "-v",
        "--var",
        dest="var",
        required=True,
        type=int,
        help="Value for the variable being changed",
    )
    arguments = vars(argument_parser.parse_args())
    return Configuration(**arguments)
