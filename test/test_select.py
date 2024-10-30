import numpy as np

from src.select import tournament_selection
from src.tree import TreeNode


def test_tournament_selection() -> None:
    fitness = np.array([9, 5, 3, 7])
    population = [TreeNode("foo"), TreeNode("bar"), TreeNode("biz"), TreeNode("buz")]

    # Selects indices [0] and [2]
    # The seed guarantees the same selection
    actual_best = tournament_selection(fitness, population)

    assert actual_best.value == "foo"
