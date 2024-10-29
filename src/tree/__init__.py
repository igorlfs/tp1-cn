from __future__ import annotations

from src.config import EPSILON


class TreeNode:
    def __init__(
        self, value: str, left: None | TreeNode = None, right: None | TreeNode = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return str(self.value)
        return f"({self.left} {self.value} {self.right})"

    def evaluate(self, row: dict[str, float]) -> float:
        if self.left is None and self.right is None:
            return row[self.value]

        left_value = self.left and self.left.evaluate(row) or 0
        right_value = self.right and self.right.evaluate(row) or 0

        if self.value == "+":
            return left_value + right_value
        if self.value == "-":
            return left_value - right_value
        if self.value == "*":
            return left_value * right_value
        if self.value == "/":
            if right_value == 0:
                return left_value / EPSILON
            return left_value / right_value

        raise NotImplementedError
