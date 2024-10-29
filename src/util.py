import numpy as np
import pandas as pd
from numpy import ndarray
from numpy.typing import NDArray

from src.tree import TreeNode


def split_df_train_test(df: pd.DataFrame) -> tuple[pd.DataFrame, ndarray]:
    return (df - df.min()) / (df.max() - df.min()), df[df.columns[-1]].to_numpy()


def get_distance_matrix(x: pd.DataFrame, tree: TreeNode) -> NDArray[np.float64]:
    distance_matrix: NDArray[np.float64] = np.zeros(shape=(len(x), len(x)))
    # TODO fazer a diferença antes ou depois?
    for i, row1 in x.iterrows():
        eval1 = tree.evaluate(row1.to_dict())
        for j, row2 in x.iterrows():
            eval2 = tree.evaluate(row2.to_dict())
            distance_matrix[i, j] = eval1 - eval2
    return distance_matrix