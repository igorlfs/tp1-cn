import pytest

from src.constants import EPSILON
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


def test_traverse() -> None:
    tree = TreeNode("foo")
    tree = TreeNode("+", tree, tree)

    nodes = tree.traverse()

    assert len(nodes) == 3  # noqa: PLR2004
    assert str(nodes[0]) == "(foo + foo)"
    assert str(nodes[1]) == "foo"
    assert str(nodes[2]) == "foo"


@pytest.fixture
def complex_tree() -> TreeNode:
    foo = TreeNode("foo")
    bar = TreeNode("bar")
    biz = TreeNode("biz")
    buz = TreeNode("buz")
    sus = TreeNode("sus")

    mul_node = TreeNode("*", left=buz, right=sus)
    buz.parent = mul_node
    sus.parent = mul_node

    plus_node = TreeNode("+", left=biz, right=mul_node)
    biz.parent = plus_node
    mul_node.parent = plus_node

    minus_node = TreeNode("-", left=bar, right=plus_node)
    bar.parent = minus_node
    plus_node.parent = minus_node

    root = TreeNode("/", left=foo, right=minus_node)
    foo.parent = root
    minus_node.parent = root

    return root


def test_depth_height_root(complex_tree: TreeNode) -> None:
    assert complex_tree.depth() == 0
    assert complex_tree.height() == 4  # noqa: PLR2004


def test_depth_height_leaf_deep(complex_tree: TreeNode) -> None:
    assert complex_tree.right
    assert complex_tree.right.right
    assert complex_tree.right.right.right
    assert complex_tree.right.right.right.right
    assert complex_tree.right.right.right.right.depth() == 4  # noqa: PLR2004
    assert complex_tree.right.right.right.right.height() == 0


def test_depth_height_leaf_shallow(complex_tree: TreeNode) -> None:
    assert complex_tree.left
    assert complex_tree.left.depth() == 1
    assert complex_tree.left.height() == 0


def test_depth_height_leaf_intermediate(complex_tree: TreeNode) -> None:
    assert complex_tree.right
    assert complex_tree.right.right
    assert complex_tree.right.right.left
    assert complex_tree.right.right.left.depth() == 3  # noqa: PLR2004
    assert complex_tree.right.right.left.height() == 0


def test_depth_height_node(complex_tree: TreeNode) -> None:
    assert complex_tree.right
    assert complex_tree.right.right
    assert complex_tree.right.right.depth() == 2  # noqa: PLR2004
    assert complex_tree.right.right.height() == 2  # noqa: PLR2004
