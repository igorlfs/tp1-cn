import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.metrics.cluster import v_measure_score

from src.config import model
from src.tree import TreeNode
from src.util import get_distance_matrix


def evaluate_fitness(x_train: pd.DataFrame, tree: TreeNode, y_train: NDArray) -> np.float64:
    distance_matrix_train = get_distance_matrix(x_train, tree)
    model.fit(distance_matrix_train)
    y_pred = model.fit_predict(distance_matrix_train)
    return np.float64(v_measure_score(y_train, y_pred))
