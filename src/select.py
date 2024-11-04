from src.globals import rng
from src.loader import config
from src.tree import TreeNode


def select_population(
    population: list[TreeNode],
    fitness: list[float],
) -> list[TreeNode]:
    """Select a new population using tournament selection."""
    selected: list[TreeNode] = []

    # we use 1 extra individual because the last operation might be a crossover
    for _ in range(config["population_size"] - config["elitism_size"] + 1):
        selected_individual = tournament_selection(fitness, population)
        selected.append(selected_individual)

    return selected


def tournament_selection(fitness: list[float], population: list[TreeNode]) -> TreeNode:
    """Select the best individual from a tournament."""
    tournament = rng.choice(len(fitness), config["tournament_size"])

    tournament_fitness: list[tuple[int, float]] = [(i, fitness[i]) for i in tournament]

    best_individual = max(tournament_fitness, key=lambda x: x[1])

    return population[best_individual[0]]
