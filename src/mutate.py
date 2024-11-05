import random

from src.globals import rng
from src.loader import config
from src.operations import Operations
from src.tree import TreeNode
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
    """Update the node's value with a random Operation. `node` must be an Operator."""
    operator = random.choice(list(Operations))
    return TreeNode(operator, node.left, node.right)


def swap_terminal(node: TreeNode, features: list[str]) -> TreeNode:
    """Update the node's value with a random feature. `node` must be a Terminal."""
    assert node.left is None and node.right is None

    feature = rng.choice(features)
    return TreeNode(feature, node.left, node.right)


def mutate_node(root: TreeNode, features: list[str]) -> TreeNode:
    """Mutate a single randomly selected node in the tree."""
    nodes = root.traverse()
    if not nodes:
        return root

    target_node = random.choice(nodes)

    if target_node.value in list(Operations):
        if random.random() < config["swap_operator_prob"]:
            return swap_operator(target_node)
        else:  # noqa: RET505
            return mutate_operator_to_terminal(target_node, features)
    else:  # noqa: PLR5501
        if random.random() < config["swap_terminal_prob"]:
            return swap_terminal(target_node, features)
        else:  # noqa: RET505
            # Keep the generated tree shallow
            return generate_random_tree(
                features,
                # The max_depth must be at least 1
                # The subtraction may be 0, if the target_node is one of the deepest leaves
                max(config["max_depth"] - target_node.depth(), 1),
                target_node.parent,
            )
