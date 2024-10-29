import numpy as np
import pandas as pd
from sklearn.utils.random import check_random_state

from src.config import POPULATION_SIZE, SEED
from src.evaluate import evaluate_fitness
from src.mutate import mutate_tree
from src.select import select_population
from src.tree.generate import generate_random_tree
from src.util import split_df_train_test

rng = check_random_state(SEED)

# TODO paramatreizar
MAX_GENERATIONS = 1
MAX_DEPTH = 7
DATA_PATH = "./data"
DATASET_PATH = f"{DATA_PATH}/breast_cancer_coimbra_"


def main() -> None:
    df_train = pd.read_csv(f"{DATASET_PATH}train.csv")

    features: list[str] = df_train.columns.to_list()

    # The last column is the Y
    features.pop()

    assert features is not None

    x_train, y_train = split_df_train_test(df_train)

    df_test = pd.read_csv(f"{DATASET_PATH}test.csv")
    x_test, y_test = split_df_train_test(df_test)

    population = [generate_random_tree(features, MAX_DEPTH) for _ in range(POPULATION_SIZE)]
    for _ in range(MAX_GENERATIONS):
        # Evaluate fitness, select, crossover, mutate, replace
        fitness = np.zeros(POPULATION_SIZE, dtype=np.float64)
        for i, tree in enumerate(population):
            fitness[i] = evaluate_fitness(x_train, tree, y_train)
        [print(i) for i in fitness]
        new_population = select_population(population, fitness)
        for i, tree in enumerate(new_population):
            fitness[i] = evaluate_fitness(x_train, tree, y_train)
        [print(i) for i in fitness]
        # print(new_population)
        # population[i] = mutate_tree(tree, features)


