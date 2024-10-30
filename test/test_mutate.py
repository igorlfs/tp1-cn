import pytest

from src.mutate import mutate_operator_to_terminal, swap_operator
from src.tree import TreeNode


def test_swap_operator() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("+", tree, tree)

    swapped_tree = swap_operator(tree)

    assert swapped_tree.value == "*"
    assert str(swapped_tree.left) == "foo"
    assert str(swapped_tree.right) == "foo"


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
