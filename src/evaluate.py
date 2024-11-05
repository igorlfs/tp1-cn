import numpy as np
import pandas as pd
from numba import jit
from numpy.typing import NDArray
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import v_measure_score

from src.tree import TreeNode


def evaluate_fitness(x: pd.DataFrame, tree: TreeNode, y: NDArray, num_labels: int) -> float:
    evaluations = [tree.evaluate(row.to_dict()) for _, row in x.iterrows()]
    distance_matrix_train = _get_distance_matrix(len(evaluations), evaluations)
    model = AgglomerativeClustering(n_clusters=num_labels, metric="precomputed", linkage="average")
    model.fit(distance_matrix_train)
    y_pred = model.fit_predict(distance_matrix_train)
    return float(v_measure_score(y, y_pred))


@jit(nopython=True)
def _get_distance_matrix(n: int, evaluations: list[float]) -> NDArray[np.float64]:
    distance_matrix: NDArray[np.float64] = np.zeros(shape=(n, n))
    for i in range(n):
        distance_matrix[i, i] = 0
        for j in range(i + 1, n):
            distance = abs(evaluations[i] - evaluations[j])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix
