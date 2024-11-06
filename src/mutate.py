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


def mutate_node(node: TreeNode, features: list[str]) -> None:
    """Mutate node in-place."""
    if node.value in list(Operations):
        if random.random() < config["swap_operator_prob"]:
            new_node = swap_operator(node)
        else:
            new_node = mutate_operator_to_terminal(node, features)
    else:  # noqa: PLR5501
        if random.random() < config["swap_terminal_prob"]:
            new_node = swap_terminal(node, features)
        else:
            new_node = generate_random_tree(
                features,
                # Keep the generated tree shallow
                # The max_depth must be at least 1
                # The subtraction may be 0, if the selected_node is one of the deepest leaves
                max(config["max_depth"] - node.depth(), 1),
                node.parent,
            )

    node.value = new_node.value
    node.left = new_node.left
    node.right = new_node.right


def mutate(root: TreeNode, features: list[str]) -> None:
    """Mutate a single randomly selected node in the tree."""
    nodes = root.traverse()

    node = random.choice(nodes)

    mutate_node(node, features)
