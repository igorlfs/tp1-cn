import pytest

from src.config import EPSILON
from src.tree import TreeNode

LEAF_VALUE = 7.0


def test_tree_evaluate_leaf() -> None:
    tree = TreeNode("foo")
    row = {"foo": 7.0}

    assert tree.evaluate(row) == LEAF_VALUE


def test_tree_evaluate_add() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("+", tree, tree)
    row = {"foo": 7.0}

    assert tree.evaluate(row) == 2 * LEAF_VALUE


def test_tree_evaluate_sub() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("-", tree, tree)
    row = {"foo": 7.0}

    assert tree.evaluate(row) == 0


def test_tree_evaluate_mul() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("*", tree, tree)
    row = {"foo": 7.0}

    assert tree.evaluate(row) == LEAF_VALUE * LEAF_VALUE


def test_tree_evaluate_div() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("/", tree, tree)
    row = {"foo": 7.0}

    assert tree.evaluate(row) == 1


def test_tree_evaluate_div_by_zero() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("/", tree, TreeNode("bar"))
    row = {"foo": 7.0, "bar": 0.0}

    assert tree.evaluate(row) == LEAF_VALUE / EPSILON


def test_tree_evaluate_not_implemented() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("|", tree, tree)
    row = {"foo": 7.0}

    with pytest.raises(NotImplementedError):
        tree.evaluate(row)
