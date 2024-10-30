import numpy as np
import pandas as pd

from src.evaluate import evaluate_fitness
from src.loader import config
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

    df_test = pd.read_csv(f"{dataset_path}test.csv")
    x_test, y_test = split_df_data_label(df_test)

    population = [
        generate_random_tree(features, config["max_depth"])
        for _ in range(config["population_size"])
    ]
    for _ in range(config["max_generations"]):
        # Evaluate fitness, select, crossover, mutate, replace
        fitness = np.zeros(config["population_size"], dtype=np.float64)
        for i, tree in enumerate(population):
            fitness[i] = evaluate_fitness(x_train, tree, y_train)
        [print(i) for i in fitness]
        new_population = select_population(population, fitness)
        for i, tree in enumerate(new_population):
            fitness[i] = evaluate_fitness(x_train, tree, y_train)
        [print(i) for i in fitness]
        # print(new_population)
        # population[i] = mutate_tree(tree, features)


