
import math

import pytest

from password_generator.strength import calculate_entropy, evaluate_strength


def test_calculate_entropy():
    entropy = calculate_entropy(
        length=16,
        pool_size=94,
    )

    expected = 16 * math.log2(94)

    assert entropy == pytest.approx(expected)


def test_calculate_entropy_rejects_invalid_length():
    with pytest.raises(ValueError):
        calculate_entropy(
            length=0,
            pool_size=94,
        )


def test_calculate_entropy_rejects_invalid_pool_size():
    with pytest.raises(ValueError):
        calculate_entropy(
            length=16,
            pool_size=0,
        )



def test_evaluate_strength_weak():
    assert evaluate_strength(20) == "Weak"


def test_evaluate_strength_medium():
    assert evaluate_strength(45) == "Medium"


def test_evaluate_strength_strong():
    assert evaluate_strength(70) == "Strong"


def test_evaluate_strength_very_strong():
    assert evaluate_strength(100) == "Very Strong"


def test_evaluate_strength_rejects_negative_entropy():
    with pytest.raises(ValueError):
        evaluate_strength(-1)



def test_evaluate_strength_boundaries():
    assert evaluate_strength(40) == "Medium"
    assert evaluate_strength(60) == "Strong"
    assert evaluate_strength(80) == "Very Strong"
