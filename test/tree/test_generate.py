from src.tree.generate import generate_random_tree

MAX_DEPTH = 5


def test_generate_tree_depth() -> None:
    tree = generate_random_tree(["foo", "bar"], MAX_DEPTH, None)

    assert tree.depth() <= MAX_DEPTH
