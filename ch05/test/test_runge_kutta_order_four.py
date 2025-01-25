#!/usr/bin/env python3
import math

from pytest import approx

from ..runge_kutta_order_four.runge_kutta_order_four import \
    runge_kutta_order_four


def test_runge_kutta_order_four() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = 0.0
    b = 2.0
    alpha = 0.5
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [
        0.5000000,
        0.8292933,
        1.2140762,
        1.6489220,
        2.1272027,
        2.6408227,
        3.1798942,
        3.7323401,
        4.2834095,
        4.8150857,
        5.3053630,
    ]

    assert obs == approx(exp, abs=1e-7)


def test_runge_kutta_order_four2() -> None:
    def func(t: float, y: float) -> float:
        return t * math.exp(3.0 * t) - 2.0 * y

    a = 0.0
    b = 1.0
    alpha = 0.0
    n = 2

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 0.2969975, 3.3143118]

    assert obs == approx(exp, abs=1e-7)


def test_runge_kutta_order_four3() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (t - y) ** 2

    a = 2.0
    b = 3.0
    alpha = 1.0
    n = 2

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.8333234, 2.4999712]

    assert obs == approx(exp, abs=1e-7)


def test_runge_kutta_order_four4() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (y / t)

    a = 1.0
    b = 2.0
    alpha = 2.0
    n = 4

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 2.7789095, 3.6081647, 4.4792846, 5.3862426]

    assert obs == approx(exp, abs=1e-7)


def test_runge_kutta_order_four5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.0 * t) + math.sin(3.0 * t)

    a = 0.0
    b = 1.0
    alpha = 1.0
    n = 4

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.329165, 1.7305336, 2.0415436, 2.1180636]

    assert obs == approx(exp, abs=1e-7)


def test_runge_kutta_order_four6() -> None:
    def func(t: float, y: float) -> float:
        return y / t - (y / t) ** 2

    a = 1.0
    b = 2.0
    alpha = 1.0
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [1.014952, 1.067262, 1.1106547, 1.1812319]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)


def test_runge_kutta_order_four7() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t + (y / t) ** 2

    a = 1.0
    b = 3.0
    alpha = 0.0
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [0.4896842, 1.6612651, 2.8764941, 5.8738386]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)


def test_runge_kutta_order_four8() -> None:
    def func(t: float, y: float) -> float:
        return -(y + 1.0) * (y + 3.0)

    a = 0.0
    b = 2.0
    alpha = -2.0
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [-1.6200576, -1.2384307, -1.1146769, -1.0359922]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)


def test_runge_kutta_order_four9() -> None:
    def func(t: float, y: float) -> float:
        return -5.0 * y + 5.0 * t**2 + 2.0 * t

    a = 0.0
    b = 1.0
    alpha = 1.0 / 3.0
    n = 10

    obs = runge_kutta_order_four(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [0.1627655, 0.2774767, 0.5001579, 1.0023207]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)
