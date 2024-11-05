import numpy as np
import pandas as pd
from numpy.testing import assert_equal

from src.util import split_df_data_label


def test_split_df_data_label() -> None:
    df = pd.DataFrame(  # noqa: PD901
        {"A": [1000, 765, 800], "B": [10, 5, 7], "C": [0.5, 0.35, 0.09], "D": [2, 1, 2]}
    )

    actual_x, actual_y, actual_num_labels = split_df_data_label(df)

    assert actual_num_labels == 2  # noqa: PLR2004

    expected_x = pd.DataFrame({"A": [1, 0.765, 0.8], "B": [1, 0.5, 0.7], "C": [1, 0.7, 0.18]})

    assert actual_x.equals(expected_x)

    assert_equal(actual_y, np.array([2, 1, 2]))
