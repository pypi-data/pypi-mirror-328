import numpy as np
from typing import List


def batch_generator(data: List, batch_size: int):
    """Generate data in fixed-size chunks"""
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


def safe_divide(numerator: np.ndarray, denominator: np.ndarray) -> np.ndarray:
    """Perform division with zero handling"""
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.true_divide(numerator, denominator)
        result[~np.isfinite(result)] = 0.0
    return result
