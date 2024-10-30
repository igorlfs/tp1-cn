import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import v_measure_score

from src.tree import TreeNode

model = AgglomerativeClustering(metric="precomputed", linkage="average")


def evaluate_fitness(x_train: pd.DataFrame, tree: TreeNode, y_train: NDArray) -> np.float64:
    distance_matrix_train = _get_distance_matrix(x_train, tree)
    model.fit(distance_matrix_train)
    y_pred = model.fit_predict(distance_matrix_train)
    return np.float64(v_measure_score(y_train, y_pred))


def _get_distance_matrix(x: pd.DataFrame, tree: TreeNode) -> NDArray[np.float64]:
    distance_matrix: NDArray[np.float64] = np.zeros(shape=(len(x), len(x)))
    # TODO fazer a diferença antes ou depois?
    for i, row1 in x.iterrows():
        eval1 = tree.evaluate(row1.to_dict())
        for j, row2 in x.iterrows():
            eval2 = tree.evaluate(row2.to_dict())
            distance_matrix[i, j] = eval1 - eval2
    return distance_matrix
