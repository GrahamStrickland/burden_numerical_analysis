#!/usr/bin/env python3
import math
from pytest import approx

from ..newton.newton import newtons_method


def test_newtons_method_trig() -> None:
    def f(x: float) -> float:
        return math.cos(x) - x

    def dx(x: float) -> float:
        return -math.sin(x) - 1.0

    p_0: float = 0.7853981633974483
    tol: float = 1e-9
    n_0: int = 5

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = 0.7390851332

    assert obs == approx(exp, abs=tol)


def test_newtons_method_poly() -> None:
    def f(x: float) -> float:
        return x**2 - 6.0

    def dx(x: float) -> float:
        return 2.0 * x

    p_0: float = 1.0
    tol: float = 1e-4
    n_0: int = 2

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = 2.60714

    assert obs == approx(exp, abs=tol)


def test_newtons_method_poly_2() -> None:
    def f(x: float) -> float:
        return x**3 - 2.0 * x**2 - 5.0

    def dx(x: float) -> float:
        return 3.0 * x**2 - 4.0 * x

    p_0: float = 2.0
    tol: float = 1e-4
    n_0: int = 5

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = 2.69065

    assert obs == approx(exp, abs=tol)


def test_newtons_method_poly_3() -> None:
    def f(x: float) -> float:
        return x**3 + 3.0 * x**2 - 1.0

    def dx(x: float) -> float:
        return 3.0 * x**2 + 6.0 * x

    p_0: float = -3.0
    tol: float = 1e-4
    n_0: int = 7

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = -2.87939

    assert obs == approx(exp, abs=tol)


def test_newtons_method_trig_2() -> None:
    def f(x: float) -> float:
        return x - math.cos(x)

    def dx(x: float) -> float:
        return 1.0 + math.sin(x)

    p_0: float = 0.0
    tol: float = 1e-4
    n_0: int = 4

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = 0.73909

    assert obs == approx(exp, abs=tol)


def test_newtons_method_trig_3() -> None:
    def f(x: float) -> float:
        return x - 0.8 - 0.2 * math.sin(x)

    def dx(x: float) -> float:
        return 1.0 - 0.2 * math.cos(x)

    p_0: float = 0.0
    tol: float = 1e-4
    n_0: int = 3

    obs = newtons_method(f, dx, p_0, tol, n_0)
    exp: float = 0.96434

    assert obs == approx(exp, abs=tol)
