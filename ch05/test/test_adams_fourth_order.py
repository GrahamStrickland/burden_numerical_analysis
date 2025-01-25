#!/usr/bin/env python3
import math

from pytest import approx

from ..adams_fourth_order.adams_fourth_order import adams_fourth_order


def test_adams_fourth_order() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = 0.0
    b = 2.0
    alpha = 0.5
    n = 10

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [
        0.5,
        0.8292933,
        1.2140762,
        1.648922,
        2.1272056,
        2.6408286,
        3.1799026,
        3.7323505,
        4.2834208,
        4.8150964,
        5.3053707,
    ]

    assert obs == approx(exp, abs=1e-7)


def test_adams_fourth_order2() -> None:
    def func(t: float, y: float) -> float:
        return t * math.exp(3.0 * t) - 2.0 * y

    a = 0.0
    b = 1.0
    alpha = 0.0
    n = 5

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 0.0269059, 0.1510468, 0.4966479, 1.3408657, 3.2450881]

    assert obs == approx(exp, abs=1e-7)


def test_adams_fourth_order3() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (t - y) ** 2

    a = 2.0
    b = 3.0
    alpha = 1.0
    n = 5

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.366661, 1.6857079, 1.9749941, 2.2446995, 2.5003083]

    assert obs == approx(exp, abs=1e-7)


def test_adams_fourth_order4() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t

    a = 1.0
    b = 2.0
    alpha = 2.0
    n = 5

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 2.6187787, 3.2710491, 3.95199, 4.6579968, 5.3862715]

    assert obs == approx(exp, abs=1e-7)


def test_adams_fourth_order5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.0 * t) + math.sin(3.0 * t)

    a = 0.0
    b = 1.0
    alpha = 1.0
    n = 5

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.252935, 1.5712383, 1.8751097, 2.0796618, 2.1192575]

    assert obs == approx(exp, abs=1e-7)


def test_adams_fourth_order6() -> None:
    def func(t: float, y: float) -> float:
        return y / t - (y / t) ** 2

    a = 1.0
    b = 2.0
    alpha = 1.0
    n = 10

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [1.014952, 1.0475227, 1.0884141, 1.1336331, 1.1812112]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[4] == approx(exp[1], abs=1e-7)
    assert obs[6] == approx(exp[2], abs=1e-7)
    assert obs[8] == approx(exp[3], abs=1e-7)
    assert obs[10] == approx(exp[4], abs=1e-7)


def test_adams_fourth_order7() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t + (y / t) ** 2

    a = 1.0
    b = 3.0
    alpha = 0.0
    n = 10

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [0.4896842, 1.1994245, 2.2134701, 3.6784144, 5.8739518]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[4] == approx(exp[1], abs=1e-7)
    assert obs[6] == approx(exp[2], abs=1e-7)
    assert obs[8] == approx(exp[3], abs=1e-7)
    assert obs[10] == approx(exp[4], abs=1e-7)


def test_adams_fourth_order8() -> None:
    def func(t: float, y: float) -> float:
        return -(y + 1.0) * (y + 3.0)

    a = 0.0
    b = 2.0
    alpha = -2.0
    n = 20

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [-1.5378788, -1.2384134, -1.0948609, -1.0359757]

    assert obs[5] == approx(exp[0], abs=1e-7)
    assert obs[10] == approx(exp[1], abs=1e-7)
    assert obs[15] == approx(exp[2], abs=1e-7)
    assert obs[20] == approx(exp[3], abs=1e-7)


def test_adams_fourth_order9() -> None:
    def func(t: float, y: float) -> float:
        return -5.0 * y + 5.0 * t**2 + 2.0 * t

    a = 0.0
    b = 1.0
    alpha = 1.0 / 3.0
    n = 10

    obs = adams_fourth_order(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [0.1627655, 0.2048557, 0.3762804, 0.6458949, 1.0021372]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[4] == approx(exp[1], abs=1e-7)
    assert obs[6] == approx(exp[2], abs=1e-7)
    assert obs[8] == approx(exp[3], abs=1e-7)
    assert obs[10] == approx(exp[4], abs=1e-7)
