#!/usr/bin/env python3
import math
from pytest import approx

from ..fixed_point.fixed_point import fixed_point


def test_fixed_point_polynomial() -> None:
    def func(x: float) -> float:
        return 0.5 * (x**3 + 1.0)

    p_0: float = 0.5
    tol: float = 1e-4
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.60917204

    assert obs == approx(exp, abs=tol)


def test_fixed_point_polynomial2() -> None:
    def func(x: float) -> float:
        return 2.0/x - 1.0/x**2

    p_0: float = 0.5
    tol: float = 1e-4
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = None

    assert obs == exp


def test_fixed_point_polynomial3() -> None:
    def func(x: float) -> float:
        return math.sqrt(2.0 - 1.0/x)

    p_0: float = 0.5
    tol: float = 1e-4
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = None

    assert obs == exp


def test_fixed_point_polynomial4() -> None:
    def func(x: float) -> float:
        return - (1.0 - 2.0*x)**(1.0/3.0)

    p_0: float = 0.5
    tol: float = 1e-4
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = -1.57197274

    assert obs == approx(exp, abs=tol)


def test_fixed_point_polynomial5() -> None:
    def func(x: float) -> float:
        return (3.0*x**2 + 3.0)**0.25

    p_0: float = 1
    tol: float = 0.01
    n_0: int = 6

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 1.94332

    assert obs == approx(exp, abs=tol)


def test_fixed_point_trig() -> None:
    def func(x: float) -> float:
        return math.pi + 0.5*math.sin(x/2.0)

    p_0: float = math.pi
    tol: float = 0.01
    n_0: int = 3

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 3.626996

    assert obs == approx(exp, abs=tol)


def test_fixed_point_sqrt() -> None:
    def func(x: float) -> float:
        return 0.5*(x+3.0/x)

    p_0: float = 1.0
    tol: float = 1e-6
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 1.73205

    assert obs == approx(exp, abs=tol)


def test_fixed_point_exponential() -> None:
    def func(x: float) -> float:
        return (2.0 - math.exp(x) + x**2) / 3.0

    p_0: float = 0
    tol: float = 1e-6
    n_0: int = 9

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.257531

    assert obs == approx(exp, abs=tol)


def test_fixed_point_polynomial6() -> None:
    def func(x: float) -> float:
        return (5.0/x**2) + 2.0

    p_0: float = 2.5
    tol: float = 1e-6
    n_0: int = 17

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 2.690650

    assert obs == approx(exp, abs=tol)


def test_fixed_point_exponential2() -> None:
    def func(x: float) -> float:
        return (math.exp(x)/3.0)**0.5

    p_0: float = 0.25
    tol: float = 1e-6
    n_0: int = 14

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.909999

    assert obs == approx(exp, abs=tol)


def test_fixed_point_power() -> None:
    def func(x: float) -> float:
        return 5.0**(-x)

    p_0: float = 0.3
    tol: float = 1e-6
    n_0: int = 39

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.469625

    assert obs == approx(exp, abs=tol)


def test_fixed_point_power2() -> None:
    def func(x: float) -> float:
        return 6.0**(-x)

    p_0: float = 0.3
    tol: float = 1e-6
    n_0: int = 48

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.448059

    assert obs == approx(exp, abs=tol)


def test_fixed_point_trig2() -> None:
    def func(x: float) -> float:
        return 0.5*(math.sin(x) + math.cos(x))

    p_0: float = 0
    tol: float = 1e-6
    n_0: int = 6

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.704812

    assert obs == approx(exp, abs=tol)


def test_fixed_point_sqrt() -> None:
    def func(x: float) -> float:
        return 0.5*(x+3.0/x)

    p_0: float = 1.0
    tol: float = 1e-6
    n_0: int = 4

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 1.73205

    assert obs == approx(exp, abs=tol)


def test_fixed_point_exponential() -> None:
    def func(x: float) -> float:
        return (2.0 - math.exp(x) + x**2) / 3.0

    p_0: float = 0
    tol: float = 1e-6
    n_0: int = 9

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.257531

    assert obs == approx(exp, abs=tol)


def test_fixed_point_polynomial6() -> None:
    def func(x: float) -> float:
        return (5.0/x**2) + 2.0

    p_0: float = 2.5
    tol: float = 1e-6
    n_0: int = 17

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 2.690650

    assert obs == approx(exp, abs=tol)


def test_fixed_point_exponential2() -> None:
    def func(x: float) -> float:
        return (math.exp(x)/3.0)**0.5

    p_0: float = 0.25
    tol: float = 1e-6
    n_0: int = 14

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.909999

    assert obs == approx(exp, abs=tol)


def test_fixed_point_power() -> None:
    def func(x: float) -> float:
        return 5.0**(-x)

    p_0: float = 0.3
    tol: float = 1e-6
    n_0: int = 39

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.469625

    assert obs == approx(exp, abs=tol)


def test_fixed_point_power2() -> None:
    def func(x: float) -> float:
        return 6.0**(-x)

    p_0: float = 0.3
    tol: float = 1e-6
    n_0: int = 48

    obs = fixed_point(func, p_0, tol, n_0)
    exp: float = 0.448059

    assert obs == approx(exp, abs=tol)
