from src.tree.generate import generate_random_tree


def test_generate_tree_depth() -> None:
    for _ in range(100):
        tree = generate_random_tree(["foo", "bar"], 5, None)

        assert tree.height() < 5  # noqa: PLR2004
