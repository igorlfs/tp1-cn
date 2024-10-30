import pytest

from src.configuration.validate import validate_probaility, validate_size


def test_validate_size() -> None:
    with pytest.raises(ValueError):
        validate_size(-1, "Foo")


def test_validate_probability_low() -> None:
    with pytest.raises(ValueError):
        validate_probaility(-1, "Foo")


def test_validate_probability_high() -> None:
    with pytest.raises(ValueError):
        validate_probaility(2, "Foo")
