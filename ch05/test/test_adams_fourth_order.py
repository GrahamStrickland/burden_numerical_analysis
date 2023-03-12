#!/usr/bin/env python3
import math
from pytest import approx

from ..adams_fourth_order.adams_fourth_order import adams_fourth_order 


def test_adams_fourth_order() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = .0
    b = 2.
    alpha = .5
    n = 10

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [.5, .8292933, 1.2140762, 1.648922, 2.1272056, 2.6408286, 3.1799026, 3.7323505,
           4.2834208, 4.8150964, 5.3053707]

    assert obs == approx(exp, abs=1e-7)
