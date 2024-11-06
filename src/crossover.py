import random

from src.loader import config
from src.tree import OptNode, TreeNode


def crossover(tree1: TreeNode, tree2: TreeNode) -> tuple[OptNode, OptNode]:
    """Perform crossover between two trees."""

    traversal1, traversal2 = tree1.traverse(), tree2.traverse()

    node1, node2 = random.choice(traversal1), random.choice(traversal2)

    # We have to assure the newly generated trees don't exceed the max depth
    # To check that, for each tree we look at its depth, which is
    # what is above in tree A + what is below tree B is less than the configured max_depth
    # the sum can't be equal either, since it only counts the edges (and excludes None nodes)
    while (
        node1.depth() + node2.height() >= config["max_depth"]
        or node1.height() + node2.depth() >= config["max_depth"]
    ):
        node1 = random.choice(traversal1)
        node2 = random.choice(traversal2)

    new_tree1 = replace_node(tree1, node1, node2)
    new_tree2 = replace_node(tree2, node2, node1)

    return new_tree1, new_tree2


def replace_node(tree: OptNode, old_node: TreeNode, new_node: TreeNode) -> OptNode:
    """Replace old_node in the tree with new_node."""
    if tree is None:
        return None

    if tree is old_node:
        new_node.parent = old_node.parent
        return new_node

    # Create a new node and recursively replace its children, setting `self` as the parent
    new_left = replace_node(tree.left, old_node, new_node)
    new_right = replace_node(tree.right, old_node, new_node)

    new_tree = TreeNode(
        tree.value,
        new_left,
        new_right,
        parent=tree.parent,  # Keep the parent consistent in the replaced structure
    )

    # Update children's parent references to this new node
    if new_left:
        new_left.parent = new_tree
    if new_right:
        new_right.parent = new_tree

    return new_tree
