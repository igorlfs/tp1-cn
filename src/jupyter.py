from sys import argv


def is_interactive() -> bool:
    """Check if running in Jupyter (or IPython)."""
    import __main__ as main

    return not hasattr(main, "__file__")


def handle_jupyter_arguments() -> None:
    """Add arguments when executing via Jupyter."""
    # Jupyter adds some default arguments when running via VSCode
    argv.clear()
    argv.extend(
        [
            "cn-tp1",  # program name, the name itself doesn't matter but it must be present
            "--seed",
            "123456",
            "--leaf-probability",
            "0.1",
            "--mutation-probability",
            "0.1",
            "--swap-terminal-prob",
            "0.4",
            "--swap-operator-probability",
            "0.4",
            "--crossover-probability",
            "0.5",
            "--population-size",
            "30",
            "--tournament-size",
            "2",
            "--elitism-size",
            "1",
            "--max-generations",
            "30",
            "--max-depth",
            "7",
            "breast_cancer_coimbra",
        ]
    )
