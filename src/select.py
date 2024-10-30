import numpy as np
from numpy.typing import NDArray

from src.globals import rng
from src.loader import config
from src.tree import TreeNode


def select_population(
    population: list[TreeNode],
    fitness: NDArray[np.float64],
) -> list[TreeNode]:
    """Select a new population using tournament selection."""
    selected: list[TreeNode] = []

    for _ in range(config["population_size"]):
        selected_individual = tournament_selection(fitness, population)
        selected.append(selected_individual)

    return selected


def tournament_selection(fitness: NDArray[np.float64], population: list[TreeNode]) -> TreeNode:
    """Select the best individual from a tournament."""
    tournament = rng.choice(len(fitness), min(config["tournament_size"], len(fitness)))

    tournament_fitness: list[tuple[int, np.float64]] = [(i, fitness[i]) for i in tournament]

    best_individual: tuple[int, np.float64] = max(tournament_fitness, key=lambda x: x[1])

    return population[best_individual[0]]
