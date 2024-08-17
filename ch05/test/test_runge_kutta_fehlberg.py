#!/usr/bin/env python3
import math
from pytest import approx

from ..runge_kutta_fehlberg.runge_kutta_fehlberg import runge_kutta_fehlberg


def test_runge_kutta_fehlberg() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = 0.0
    b = 2.0
    alpha = 0.5
    tol = 1e-5
    hmax = 0.25
    hmin = 0.01

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [
        0.5000000,
        0.9204886,
        1.3964910,
        1.9537488,
        2.5864260,
        3.2604605,
        3.9520955,
        4.6308268,
        5.2574861,
        5.3054896,
    ]

    assert obs == approx(exp, abs=tol)


def test_runge_kutta_fehlberg2() -> None:
    def func(t: float, y: float) -> float:
        return t * math.exp(3.0 * t) - 2.0 * y

    a = 0.0
    b = 1.0
    alpha = 0.0
    tol = 1e-4
    hmax = 0.25
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [0.0298184, 0.4016438, 1.5894061, 3.2190497]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[3] == approx(exp[1], abs=tol)
    assert obs[5] == approx(exp[2], abs=tol)
    assert obs[7] == approx(exp[3], abs=tol)


def test_runge_kutta_fehlberg3() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (t - y) ** 2

    a = 2.0
    b = 3.0
    alpha = 1.0
    tol = 1e-4
    hmax = 0.25
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [1.4499988, 1.8333332, 2.1785718, 2.5000005]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[2] == approx(exp[1], abs=tol)
    assert obs[3] == approx(exp[2], abs=tol)
    assert obs[4] == approx(exp[3], abs=tol)


def test_runge_kutta_fehlberg4() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t

    a = 1.0
    b = 2.0
    alpha = 2.0
    tol = 1e-4
    hmax = 0.25
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [2.7789299, 3.6081985, 4.4793288, 5.3862958]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[2] == approx(exp[1], abs=tol)
    assert obs[3] == approx(exp[2], abs=tol)
    assert obs[4] == approx(exp[3], abs=tol)


def test_runge_kutta_fehlberg5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.0 * t) + math.sin(3.0 * t)

    a = 0.0
    b = 1.0
    alpha = 1.0
    tol = 1e-4
    hmax = 0.25
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [1.3291478, 1.7304857, 2.0414669, 2.117975]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[2] == approx(exp[1], abs=tol)
    assert obs[3] == approx(exp[2], abs=tol)
    assert obs[4] == approx(exp[3], abs=tol)


def test_runge_kutta_fehlberg6() -> None:
    def func(t: float, y: float) -> float:
        return y / t - (y / t) ** 2

    a = 1.0
    b = 4.0
    alpha = 1.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [1.0051237, 1.1213948, 1.2795396, 1.6762393]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[5] == approx(exp[1], abs=tol)
    assert obs[7] == approx(exp[2], abs=tol)
    assert obs[11] == approx(exp[3], abs=tol)


def test_runge_kutta_fehlberg7() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t + (y / t) ** 2

    a = 1.0
    b = 3.0
    alpha = 0.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [0.7234123, 1.3851234, 2.1673514, 4.1297939, 5.8741059]

    assert obs[4] == approx(exp[0], abs=tol)
    assert obs[7] == approx(exp[1], abs=tol)
    assert obs[10] == approx(exp[2], abs=tol)
    assert obs[16] == approx(exp[3], abs=tol)
    assert obs[21] == approx(exp[4], abs=tol)


def test_runge_kutta_fehlberg8() -> None:
    def func(t: float, y: float) -> float:
        return -(y + 1.0) * (y + 3.0)

    a = 0.0
    b = 3.0
    alpha = -2.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [-1.8380836, -1.3597623, -1.1684827, -1.0749509, -1.0291158, -1.004945]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[5] == approx(exp[1], abs=tol)
    assert obs[9] == approx(exp[2], abs=tol)
    assert obs[13] == approx(exp[3], abs=tol)
    assert obs[17] == approx(exp[4], abs=tol)
    assert obs[23] == approx(exp[5], abs=tol)


def test_runge_kutta_fehlberg9() -> None:
    def func(t: float, y: float) -> float:
        return (t + 2.0 * t**3) * y**3 - t * y

    a = 0.0
    b = 2.0
    alpha = 1.0 / 3.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.05

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [0.3108201, 0.2221189, 0.1133085, 0.0543454]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[3] == approx(exp[1], abs=tol)
    assert obs[5] == approx(exp[2], abs=tol)
    assert obs[8] == approx(exp[3], abs=tol)
