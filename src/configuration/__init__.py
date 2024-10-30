from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from src.datasets import Datasets


@dataclass
class Configuration(TypedDict):
    seed: int

    leaf_prob: float
    mutation_prob: float

    population_size: int
    tournament_size: int
    elitism_size: int

    max_generations: int
    max_depth: int

    dataset: Datasets
