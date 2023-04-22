#!/usr/bin/env python3
import math
from pytest import approx

from ..adams_variable_step.adams_variable_step import adams_variable_step


def test_adams_variable_step() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = .0
    b = 2.
    alpha = .5
    tol = 1e-5
    hmax = .2
    hmin = .01

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
        )
    exp = [.5, .70480402, .93320019, 1.18390218, 1.45544767, 1.74617341, 2.05418856,
           2.37734317, 2.71319271, 3.05895769, 3.41147778, 3.70412572, 3.99667414,
           4.28662249, 4.57119105, 4.84729107, 5.11148918, 5.16093546, 5.20976475,
           5.25794701, 5.30545159] 

    assert obs == approx(exp, abs=tol)
