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
from src.select import select
from src.tree import TreeNode


def evolution_loop(
    population: list[TreeNode],
    x_train: DataFrame,
    y_train: NDArray,
    num_labels: int,
    features: list[str],
) -> tuple[list[TreeNode], list[float]]:
    df_dict: list[dict[str, float]] = [row.to_dict() for _, row in x_train.iterrows()]

    fitness = [evaluate_fitness(df_dict, tree, y_train, num_labels) for tree in population]

    if config["verbose"]:
        print("Generation,BestFit,AvgFit,WorstFit,Repetitions,ChildImproved,ChildWorsened")

    for i in range(config["max_generations"]):
        str_representations = [str(tree) for tree in population]
        repetitions = config["population_size"] - len(set(str_representations))

        avg = np.average(fitness)
        children_improved = 0
        children_worsened = 0

        next_generation, next_fitness = elitism(population, fitness, config["elitism_size"])

        candidates = select(population, fitness)

        j = 0
        while len(next_generation) < config["population_size"]:
            if rng.random() < config["crossover_prob"]:
                parent1 = deepcopy(candidates[j])
                parent2 = deepcopy(candidates[j + 1])

                avg_fitness_parents = 0.5 * (fitness[j] + fitness[j + 1])

                offspring1, offspring2 = crossover(parent1, parent2)

                assert offspring1 is not None and offspring2 is not None

                next_fitness.append(evaluate_fitness(df_dict, offspring1, y_train, num_labels))

                if next_fitness[-1] > avg_fitness_parents:
                    children_improved += 1
                else:
                    children_worsened += 1

                next_fitness.append(evaluate_fitness(df_dict, offspring2, y_train, num_labels))

                if next_fitness[-1] > avg_fitness_parents:
                    children_improved += 1
                else:
                    children_worsened += 1

                j += 2

                next_generation.extend([offspring1, offspring2])
            else:
                tree = deepcopy(candidates[j])

                mutate(tree, features)

                next_fitness.append(evaluate_fitness(df_dict, tree, y_train, num_labels))

                if next_fitness[-1] > fitness[j]:
                    children_improved += 1
                else:
                    children_worsened += 1

                j += 1

                next_generation.append(tree)

        if config["verbose"]:
            print(
                f"G{i},{max(fitness)},{avg},{min(fitness)},{repetitions},{children_improved},{children_worsened}"
            )

        population = next_generation[: config["population_size"]]  # might have an extra offspring
        fitness = next_fitness[: config["population_size"]]

    return population, fitness
