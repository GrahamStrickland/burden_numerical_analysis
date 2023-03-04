#!/usr/bin/env python3
import math
from pytest import approx

from ..modified_eulers_method.modified_eulers_method import modified_eulers_method


def test_modified_eulers_method() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a: float = 0.0
    b: float = 2.0
    alpha: float = 0.5
    n: int = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp: list[float] = [0.5000000, 0.8260000, 1.2069200, 1.6372424, 2.1102357, 2.6176876,
                        3.1495789, 3.6936862, 4.2350972, 4.7556185, 5.2330546]

    assert obs == approx(exp, abs=1e-7)
