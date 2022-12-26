#!/usr/bin/env python3
import math
from pytest import approx

from ..bisection.bisection import bisect


def test_bisection_polynomial() -> None:
    def func(x: float) -> float:
        return x**3 + 4.0*x**2 - 10.0

    a: float = 1.0
    b: float = 2.0
    tol: float = 1e-4
    n_0: int = 15

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 1.365112305

    assert obs == approx(exp, abs=tol)


def test_bisection_trig_polynomial() -> None:
    def func(x: float) -> float:
        return math.sqrt(x) - math.cos(x)

    a: float = 0.0
    b: float = 1.0
    tol: float = 1e-3
    n_0: int = 3

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 0.625

    assert obs == approx(exp, abs=tol)


def test_bisection_polynomial2() -> None:
    def func(x: float) -> float:
        return x**3 - 7.0*x**2 + 14.0*x - 6.0

    a: float = 0.0
    b: float = 1.0
    tol: float = 1e-2
    n_0: int = 10

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 0.5859

    assert obs == approx(exp, abs=tol)


def test_bisection_polynomial3() -> None:
    def func(x: float) -> float:
        return x**3 - 7.0*x**2 + 14.0*x - 6.0

    a: float = 1.0
    b: float = 3.2
    tol: float = 1e-2
    n_0: int = 10

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 3.002

    assert obs == approx(exp, abs=tol)


def test_bisection_polynomial4() -> None:
    def func(x: float) -> float:
        return x**3 - 7.0*x**2 + 14.0*x - 6.0

    a: float = 3.2
    b: float = 4.0
    tol: float = 1e-2
    n_0: int = 10

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 3.419

    assert obs == approx(exp, abs=tol)


def test_bisection_power() -> None:
    def func(x: float) -> float:
        return x - 2.0**(-x)

    a: float = 0.0
    b: float = 1.0
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 0.641182

    assert obs == approx(exp, abs=tol)


def test_bisection_exponential() -> None:
    def func(x: float) -> float:
        return math.exp(x) - x**2 + 3.0*x - 2.0

    a: float = 0.0
    b: float = 1.0
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 0.257530

    assert obs == approx(exp, abs=tol)


def test_bisection_trig_polynomial2() -> None:
    def func(x: float) -> float:
        return 2.0*x*math.cos(2.0*x) - (x + 1.0)**2

    a: float = -3.0
    b: float = -2.0
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = -2.191307

    assert obs == approx(exp, abs=tol)


def test_bisection_trig_polynomial3() -> None:
    def func(x: float) -> float:
        return 2.0*x*math.cos(2.0*x) - (x + 1.0)**2

    a: float = -1.0
    b: float = 0.0
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = -0.798164

    assert obs == approx(exp, abs=tol)


def test_bisection_trig_polynomial4() -> None:
    def func(x: float) -> float:
        return x*math.cos(x) - 2.0*x**2 + 3.0*x - 1.0

    a: float = 0.2
    b: float = 0.3
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 0.297528

    assert obs == approx(exp, abs=tol)


def test_bisection_trig_polynomial5() -> None:
    def func(x: float) -> float:
        return x*math.cos(x) - 2.0*x**2 + 3.0*x - 1.0

    a: float = 1.2
    b: float = 1.3
    tol: float = 1e-5
    n_0: int = 20

    obs = bisect(func, a, b, tol, n_0)
    exp: float = 1.256622

    assert obs == approx(exp, abs=tol)
