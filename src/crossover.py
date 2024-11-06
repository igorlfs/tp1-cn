import random

from src.tree import OptNode, TreeNode


def crossover(tree1: TreeNode, tree2: TreeNode) -> tuple[OptNode, OptNode]:
    """Perform crossover between two trees."""

    node1 = random.choice(tree1.traverse())
    node2 = random.choice(tree2.traverse())

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
