from src.tree import TreeNode


def elitism(population: list[TreeNode], fitness: list[float], elite_count: int) -> list[TreeNode]:
    """Return the top individuals from the population."""
    sorted_population = sorted(
        zip(population, fitness, strict=True), key=lambda x: x[1], reverse=True
    )
    return [i for i, _ in sorted_population[:elite_count]]
