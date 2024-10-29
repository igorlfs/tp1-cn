import pytest

from src.mutate import mutate_operator_to_terminal
from src.tree import TreeNode


def test_mutate_operator_to_terminal() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("+", tree, tree)

    actual_tree = mutate_operator_to_terminal(tree, ["foo"])

    assert actual_tree.value == "foo"
    assert actual_tree.depth() == 1


def test_cant_mutate_operator_to_terminal_with_terminal() -> None:
    tree = TreeNode("foo")

    with pytest.raises(AssertionError):
        mutate_operator_to_terminal(tree, ["foo"])


def test_cant_mutate_operator_to_terminal_with_terminal_with_children() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("foo", tree, tree)

    with pytest.raises(ValueError):
        mutate_operator_to_terminal(tree, ["foo"])
