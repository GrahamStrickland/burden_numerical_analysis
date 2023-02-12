#!/usr/bin/env python3
import math
from pytest import approx

from ..eulers_method.eulers_method import eulers_method


def test_eulers_method() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a: float = 0.0
    b: float = 2.0
    alpha: float = 0.5
    n: int = 10

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp: list[float] = [0.5000000, 0.8000000, 1.1520000, 1.5504000, 1.9884800, 2.4581760,
                        2.9498112, 3.4517734, 3.9501281, 4.4281538, 4.8657845]

    assert obs == approx(exp, abs=1e-7)
