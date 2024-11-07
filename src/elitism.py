from src.tree import TreeNode


def elitism(
    population: list[TreeNode], fitness: list[float], elite_count: int
) -> tuple[list[TreeNode], list[float]]:
    """Return the top individuals from the population."""
    sorted_population = sorted(
        zip(population, fitness, strict=True), key=lambda x: x[1], reverse=True
    )
    return [i for i, _ in sorted_population[:elite_count]], [
        j for _, j in sorted_population[:elite_count]
    ]
