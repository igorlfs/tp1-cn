from src.globals import rng
from src.loader import config
from src.operations import Operations
from src.tree import TreeNode


def generate_random_tree(features: list[str], max_depth: int) -> TreeNode:
    if max_depth <= 1 or rng.random() < config["leaf_prob"]:
        return TreeNode(rng.choice(features))
    operator = rng.choice(list(Operations))
    left_subtree = generate_random_tree(features, max_depth - 1)
    right_subtree = generate_random_tree(features, max_depth - 1)
    return TreeNode(operator, left_subtree, right_subtree)
