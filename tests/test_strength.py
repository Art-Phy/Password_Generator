
import math

import pytest

from password_generator.strength import calculate_entropy


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
