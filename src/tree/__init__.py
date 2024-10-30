from __future__ import annotations

from src.constants import EPSILON
from src.operations import Operations


class TreeNode:
    def __init__(
        self, value: str, left: None | TreeNode = None, right: None | TreeNode = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return self.value
        return f"({self.left} {self.value} {self.right})"

    def evaluate(self, row: dict[str, float]) -> float:
        if self.left is None and self.right is None:
            return row[self.value]

        left_value = self.left and self.left.evaluate(row) or 0
        right_value = self.right and self.right.evaluate(row) or 0

        match self.value:
            case Operations.ADD:
                return left_value + right_value
            case Operations.SUB:
                return left_value - right_value
            case Operations.MUL:
                return left_value * right_value
            case Operations.DIV:
                # TODO Can I use the shorthand syntax here?
                if right_value == 0:
                    return left_value / EPSILON
                return left_value / right_value
            case _:
                raise NotImplementedError

    # TODO We could limit the MAX_DEPTH by using this property
    def depth(self) -> int:
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
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
