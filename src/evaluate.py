import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import v_measure_score

from src.tree import TreeNode

model = AgglomerativeClustering(metric="precomputed", linkage="average")


def evaluate_fitness(x: pd.DataFrame, tree: TreeNode, y: NDArray) -> float:
    evaluations = [tree.evaluate(row.to_dict()) for _, row in x.iterrows()]
    distance_matrix_train = _get_distance_matrix(len(x), evaluations)
    model.fit(distance_matrix_train)
    y_pred = model.fit_predict(distance_matrix_train)
    return float(v_measure_score(y, y_pred))


def _get_distance_matrix(n: int, evaluations: list[float]) -> NDArray[np.float64]:
    distance_matrix: NDArray[np.float64] = np.zeros(shape=(n, n))
    # TODO fazer a diferença antes ou depois?
    for i in range(n):
        for j in range(i, n):
            distance = abs(evaluations[i] - evaluations[j])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix
