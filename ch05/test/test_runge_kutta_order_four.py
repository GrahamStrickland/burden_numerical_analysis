#!/usr/bin/env python3
import math
from pytest import approx

from ..runge_kutta_order_four.runge_kutta_order_four import runge_kutta_order_four


def test_runge_kutta_order_four() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = .0
    b = 2.
    alpha = .5
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [.5000000, .8292933, 1.2140762, 1.6489220, 2.1272027, 2.6408227,
           3.1798942, 3.7323401, 4.2834095, 4.8150857, 5.3053630]

    assert obs == approx(exp, abs=1e-7)
