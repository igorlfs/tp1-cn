from copy import deepcopy

import numpy as np
from numpy.typing import NDArray
from pandas import DataFrame

from src.crossover import crossover
from src.elitism import elitism
from src.evaluate import evaluate_fitness
from src.globals import rng
from src.loader import config
from src.mutate import mutate
from src.select import select_population
from src.tree import TreeNode


def evolution_loop(
    population: list[TreeNode],
    x_train: DataFrame,
    y_train: NDArray,
    num_labels: int,
    features: list[str],
) -> tuple[list[TreeNode], list[float]]:
    fitness = []  # avoid type error that fitness isn't initialized

    if config["verbose"]:
        print("Generation,BestFit,AvgFit,WorstFit,Repetitions,ChildImproved,ChildWorsened")

    for i in range(config["max_generations"]):
        fitness = [evaluate_fitness(x_train, tree, y_train, num_labels) for tree in population]
        str_representations = [str(tree) for tree in population]
        repetitions = config["population_size"] - len(set(str_representations))

        avg = np.average(fitness)
        children_improved = 0
        children_worsened = 0

        next_generation = elitism(population, fitness, config["elitism_size"])

        candidates = select_population(population, fitness)

        j = 0
        while len(next_generation) < config["population_size"]:
            if rng.random() < config["crossover_prob"]:
                parent1 = deepcopy(candidates[j])
                parent2 = deepcopy(candidates[j + 1])

                avg_parents = 0.5 * (fitness[j] + fitness[j + 1])

                j += 2

                offspring1, offspring2 = crossover(parent1, parent2)

                assert offspring1 is not None and offspring2 is not None

                if rng.random() >= config["crossover_prob"]:
                    mutate(offspring1, features)
                    mutate(offspring2, features)

                if evaluate_fitness(x_train, offspring1, y_train, num_labels) > avg_parents:
                    children_improved += 1
                else:
                    children_worsened += 1

                if evaluate_fitness(x_train, offspring2, y_train, num_labels) > avg_parents:
                    children_improved += 1
                else:
                    children_worsened += 1

                next_generation.extend([offspring1, offspring2])
            else:
                tree = deepcopy(candidates[j])
                j += 1
                mutate(tree, features)
                next_generation.append(tree)

        if config["verbose"]:
            print(
                f"G{i},{max(fitness)},{avg},{min(fitness)},{repetitions},{children_improved},{children_worsened}"
            )

        population = next_generation[: config["population_size"]]  # might have an extra offspring

    return population, fitness
