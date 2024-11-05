from __future__ import annotations

from src.constants import EPSILON
from src.operations import Operations


class TreeNode:
    def __init__(
        self,
        value: str | Operations,
        left: None | TreeNode = None,
        right: None | TreeNode = None,
        parent: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return self.value
        if isinstance(self.value, Operations):
            return f"({self.left} {self.value.value} {self.right})"
        return f"({self.left} {self.value} {self.right})"

    def to_dot(self) -> str:
        """Generate Graphviz dot format string for the tree."""
        label = self.value.value if isinstance(self.value, Operations) else self.value
        dot_str = f'"{id(self)}" [label="{label}"];\n'
        if self.left is not None:
            dot_str += f'"{id(self)}" -> "{id(self.left)}";\n'
            dot_str += self.left.to_dot()
        if self.right is not None:
            dot_str += f'"{id(self)}" -> "{id(self.right)}";\n'
            dot_str += self.right.to_dot()
        return dot_str

    def evaluate(self, row: dict[str, float]) -> float:
        if self.left is None and self.right is None:
            return row[self.value]

        left_value = self.left and self.left.evaluate(row) or 0
        right_value = self.right and self.right.evaluate(row) or 0

        match self.value:
            case Operations.ADD:
                return float(left_value + right_value)
            case Operations.SUB:
                return float(left_value - right_value)
            case Operations.MUL:
                return float(left_value * right_value)
            case Operations.DIV:
                return float(left_value / EPSILON if right_value == 0 else left_value / right_value)
            case _:
                raise NotImplementedError

    def depth(self) -> int:
        if self.parent is None:
            return 1
        return self.parent.depth() + 1

    def height(self) -> int:
        left_depth = self.left.height() if self.left else 0
        right_depth = self.right.height() if self.right else 0
        return max(left_depth, right_depth) + 1

    def _traverse(self, nodes: list[TreeNode]) -> list[TreeNode]:
        if self is not None:
            nodes.append(self)
            if self.left:
                self.left._traverse(nodes)
            if self.right:
                self.right._traverse(nodes)
        return nodes

    def traverse(self) -> list[TreeNode]:
        nodes = []
        return self._traverse(nodes)


OptNode = TreeNode | None
