from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Configuration(TypedDict):
    seed: int

    leaf_prob: float
    mutation_prob: float

    population_size: int
    tournament_size: int
    elitism_size: int
