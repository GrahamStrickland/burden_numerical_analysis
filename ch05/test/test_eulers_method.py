#!/usr/bin/env python3
import math
from pytest import approx

from ..eulers_method.eulers_method import eulers_method


def test_eulers_method() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = .0
    b = 2.
    alpha = .5
    n = 10

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [.5000000, 0.8000000, 1.1520000, 1.5504000, 1.9884800, 2.4581760,
           2.9498112, 3.4517734, 3.9501281, 4.4281538, 4.8657845]

    assert obs == approx(exp, abs=1e-7)


def test_eulers_method_2() -> None:
    def func(t: float, y: float) -> float:
        return t*math.exp(3.0*t) - 2.0*y

    a = .0
    b = 1.
    alpha = .0
    n = 2

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, .0000000, 1.1204223]

    assert obs == approx(exp, abs=1e-7)


def test_eulers_method_3() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (t-y)**2

    a = 2.
    b = 3.
    alpha = 1.
    n = 2

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 2.0000000, 2.6250000]

    assert obs == approx(exp, abs=1e-7)


def test_eulers_method_4() -> None:
    def func(t: float, y: float) -> float:
        return 1 + y/t

    a = 1.
    b = 2.
    alpha = 2.
    n = 4

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 2.7500000, 3.5500000, 4.3916667, 5.2690476]

    assert obs == approx(exp, abs=1e-7)


def test_eulers_method_5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.0*t) + math.sin(3.0*t)

    a = 0.
    b = 1.
    alpha = 1.
    n = 4

    obs = eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.2500000, 1.6398053, 2.0242547, 2.2364573]

    assert obs == approx(exp, abs=1e-7)
