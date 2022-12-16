#!/usr/bin/env python3
from pytest import approx

from ..bisection.bisection import bisect


def test_bisection() -> None:
    def func(x: float) -> float:
        return x**3 + 4.0*x**2 - 10.0

    a: float = 1.0
    b: float = 2.0
    tol: float = 1e-4
    n0: int = 15

    obs = bisect(func, a, b, tol, n0)
    exp: float = 1.365112305

    assert obs == approx(exp)
