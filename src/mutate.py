import random

from src.globals import rng
from src.loader import config
from src.operations import Operations
from src.tree import OptNode, TreeNode
from src.tree.generate import generate_random_tree


def mutate_operator_to_terminal(node: TreeNode, features: list[str]) -> TreeNode:
    """Replace an operator node with a terminal node. `node` must be an Operator."""
    # Since node is an Operator, it should have children
    assert node.left is not None and node.right is not None

    if node.value in list(Operations):
        return TreeNode(rng.choice(features))

    # Likewise, if the node is not an Operator, it shouldn't have children
    raise ValueError


def swap_operator(node: TreeNode) -> TreeNode:
    operator = random.choice(list(Operations))  # noqa: S311
    return TreeNode(operator, node.left, node.right)


def mutate_node(node: OptNode, features: list[str]) -> OptNode:
    """Mutate a node with a given probability."""
    if node is None:
        return None

    if rng.random() < config["mutation_prob"]:
        if node.value in list(Operations):
            if rng.random() < config["reduction_prob"]:
                return mutate_operator_to_terminal(node, features)
            else:  # noqa: RET505
                return swap_operator(node)
        else:
            # TODO there must a better way to keep it shallow
            return generate_random_tree(features, max_depth=2)  # Keep it shallow

    node.left = mutate_node(node.left, features)
    node.right = mutate_node(node.right, features)

    return node


def mutate_tree(tree: TreeNode, features: list[str]) -> TreeNode:
    """Perform mutation on the entire tree."""
    mutated_tree = mutate_node(tree, features)

    assert mutated_tree is not None

    return mutated_tree
