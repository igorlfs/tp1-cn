from src.config import GENERATE_LEAF_PROBABILITY, OPERATIONS, rng
from src.tree import TreeNode


def generate_random_tree(features: list[str], max_depth: int) -> TreeNode:
    if max_depth == 1 or rng.random() < GENERATE_LEAF_PROBABILITY:
        return TreeNode(rng.choice(features))
    operator = rng.choice(OPERATIONS)
    left_subtree = generate_random_tree(features, max_depth - 1)
    right_subtree = generate_random_tree(features, max_depth - 1)
    return TreeNode(operator, left_subtree, right_subtree)
