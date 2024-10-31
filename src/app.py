import random
from copy import deepcopy

import pandas as pd

from src.crossover import crossover
from src.elitism import elitism
from src.evaluate import evaluate_fitness
from src.globals import rng
from src.loader import config
from src.mutate import mutate_tree
from src.select import select_population
from src.tree.generate import generate_random_tree
from src.util import split_df_data_label


def main() -> None:
    dataset_path = config["dataset"].get_path()
    df_train = pd.read_csv(f"{dataset_path}train.csv")

    features: list[str] = df_train.columns.to_list()

    # The last column is the label
    features.pop()

    assert features is not None

    x_train, y_train = split_df_data_label(df_train)

    population = [
        generate_random_tree(features, config["max_depth"])
        for _ in range(config["population_size"])
    ]

    for i in range(config["max_generations"]):
        fitness = [evaluate_fitness(x_train, tree, y_train) for tree in population]

        print(f"G{i}: Fit Best = {max(fitness)}")

        candidates = select_population(population, fitness)
        next_generation = elitism(population, fitness, config["elitism_size"])

        while len(next_generation) < config["population_size"]:
            if rng.random() < config["crossover_prob"]:
                parent1 = deepcopy(random.choice(candidates))  # noqa: S311
                parent2 = deepcopy(random.choice(candidates))  # noqa: S311
                offspring1, offspring2 = crossover(parent1, parent2)
                assert offspring1 is not None and offspring2 is not None
                next_generation.extend([offspring1, offspring2])
            else:
                tree = deepcopy(random.choice(candidates))  # noqa: S311
                mutated = mutate_tree(tree, features)
                next_generation.append(mutated)

        population = next_generation[: config["population_size"]]  # might have an extra offspring

    best_tree = population[fitness.index(max(fitness))]

    df_test = pd.read_csv(f"{dataset_path}test.csv")
    x_test, y_test = split_df_data_label(df_test)

    fitness_test = evaluate_fitness(x_test, best_tree, y_test)
    print(f"Test Fitness = {fitness_test}")
