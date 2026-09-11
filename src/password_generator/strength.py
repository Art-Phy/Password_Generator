
import math


def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculate the estimated entropy of a generated password"""

    if length <= 0:
        raise ValueError("Password length must be greater than zero")

    if pool_size <= 0:
        raise ValueError("Character pool size must be greater than zero")

    return length * math.log2(pool_size)



def evaluate_strength(entropy: float) -> str:
    """Return a human-readable password strength rating"""

    if entropy < 0:
        raise ValueError("Entropy cannot be negative")

    if entropy < 40:
        return "Weak"

    if entropy < 60:
        return "Medium"

    if entropy < 80:
        return "Strong"

    return "Very Strong"
