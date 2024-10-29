import numpy as np
from numpy.typing import NDArray

from src.config import ELITISM_SIZE, POPULATION_SIZE, TOURNAMENT_SIZE, rng
from src.tree import TreeNode


def select_population(
    population: list[TreeNode],
    fitness: NDArray[np.float64],
) -> list[TreeNode]:
    """Select a new population using tournament selection."""
    selected: list[TreeNode] = []

    if ELITISM_SIZE > 0:
        fitness_with_index = list(enumerate(fitness))
        sorted_fitness = sorted(fitness_with_index, key=lambda x: x[1], reverse=True)
        selected.extend([population[x[0]] for x in sorted_fitness[:ELITISM_SIZE]])

    for _ in range(POPULATION_SIZE - ELITISM_SIZE):
        selected_individual = tournament_selection(fitness, population)
        selected.append(selected_individual)

    return selected


def tournament_selection(fitness: NDArray[np.float64], population: list[TreeNode]) -> TreeNode:
    """Select the best individual from a tournament."""
    tournament = rng.choice(len(fitness), min(TOURNAMENT_SIZE, len(fitness)))

    tournament_fitness: list[tuple[int, np.float64]] = [(i, fitness[i]) for i in tournament]

    best_individual: tuple[int, np.float64] = max(tournament_fitness, key=lambda x: x[1])

    return population[best_individual[0]]
