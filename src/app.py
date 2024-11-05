import pandas as pd

from src.evaluate import evaluate_fitness
from src.genetic_programming import evolution_loop
from src.loader import config
from src.tree.generate import generate_random_tree
from src.util import split_df_data_label


def main() -> None:
    if config["verbose"]:
        print("#", config)

    dataset_path = config["dataset"].get_path()

    df_train = pd.read_csv(f"{dataset_path}train.csv")
    x_train, y_train, num_labels = split_df_data_label(df_train)

    features = df_train.columns.to_list()

    # The last column is the label
    features.pop()

    population = [
        generate_random_tree(features, config["max_depth"])
        for _ in range(config["population_size"])
    ]

    population, fitness = evolution_loop(population, x_train, y_train, num_labels, features)

    best_tree = population[fitness.index(max(fitness))]

    df_test = pd.read_csv(f"{dataset_path}test.csv")
    x_test, y_test, _ = split_df_data_label(df_test)

    fitness_test = evaluate_fitness(x_test, best_tree, y_test, num_labels)

    if config["verbose"]:
        print(f"T,{fitness_test},0,0,0,0,0")
    else:
        print(fitness_test)
