import random

from src.tree import OptNode, TreeNode


def crossover(tree1: OptNode, tree2: OptNode) -> tuple[OptNode, OptNode]:
    """Perform crossover between two trees."""

    node1 = random.choice(tree1.traverse()) if tree1 else None  # noqa: S311
    node2 = random.choice(tree2.traverse()) if tree2 else None  # noqa: S311

    new_tree1 = replace_node(tree1, node1, node2)
    new_tree2 = replace_node(tree2, node2, node1)

    return new_tree1, new_tree2


def replace_node(tree: OptNode, old_node: OptNode, new_node: OptNode) -> OptNode:
    """Replace old_node in the tree with new_node."""
    if tree is None:
        return None

    if tree is old_node:
        return new_node

    return TreeNode(
        tree.value,
        replace_node(tree.left, old_node, new_node),
        replace_node(tree.right, old_node, new_node),
    )
