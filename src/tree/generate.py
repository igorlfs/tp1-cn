import random

from src.globals import rng
from src.loader import config
from src.operations import Operations
from src.tree import OptNode, TreeNode


def generate_random_tree(features: list[str], max_depth: int, parent: OptNode) -> TreeNode:
    if max_depth == 1 or rng.random() < config["leaf_prob"]:
        return TreeNode(rng.choice(features), parent=parent)
    operator = random.choice(list(Operations))
    node = TreeNode(value=operator, parent=parent)
    node.left = generate_random_tree(features, max_depth - 1, parent=node)
    node.right = generate_random_tree(features, max_depth - 1, parent=node)
    return node
