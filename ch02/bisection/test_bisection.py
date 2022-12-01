#!/usr/bin/env python3
from pytest import approx

from ..bisection import bisection


def test_bisection() -> None:
    def function(x: float) -> float:
        return x**3 + 4.0*x**2 - 10.0

    bisect = bisection.Bisection(function)

    a: float = 1.0
    b: float = 2.0
    tol: float = 1e-4
    n_0: int = 15

    obs = bisect.bisect(a, b, tol, n_0)
    exp: float = 1.365112305

    assert obs == approx(exp)
