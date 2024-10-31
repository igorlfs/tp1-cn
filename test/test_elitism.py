from src.elitism import elitism
from src.tree import TreeNode

Tree = TreeNode


def test_elitism() -> None:
    population = [Tree("a"), Tree("b"), Tree("c"), Tree("d"), Tree("e"), Tree("f")]
    fitness = [0.5, 0.3, 0.2, 0.4, 0.8, 0.4]
    size = 3

    elite = elitism(population, fitness, size)

    assert len(elite) == size

    assert elite[0].value == "e"
    assert elite[1].value == "a"
    assert elite[2].value == "d"
