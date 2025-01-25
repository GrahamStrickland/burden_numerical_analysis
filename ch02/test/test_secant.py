#!/usr/bin/env python3
import math

from pytest import approx

from ..secant.secant import secant_method


def test_secant_method_trig() -> None:
    def f(x: float) -> float:
        return math.cos(x) - x

    p_0: float = 0.5
    p_1: float = 0.7853981634
    tol: float = 1e-10
    n_0: int = 5

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = 0.7390851332

    assert obs == approx(exp, abs=tol)


def test_secant_method_poly() -> None:
    def f(x: float) -> float:
        return x**2 - 6.0

    p_0: float = 3.0
    p_1: float = 2.0
    tol: float = 1e-5
    n_0: int = 3

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = 2.45454

    assert obs == approx(exp, abs=tol)


def test_secant_method_poly_2() -> None:
    def f(x: float) -> float:
        return x**3 - 2.0 * x**2 - 5.0

    p_0: float = 1.0
    p_1: float = 4.0
    tol: float = 1e-5
    n_0: int = 11

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = 2.69065

    assert obs == approx(exp, abs=tol)


def test_secant_method_poly_3() -> None:
    def f(x: float) -> float:
        return x**3 + 3.0 * x**2 - 1.0

    p_0: float = -3.0
    p_1: float = -2.0
    tol: float = 1e-5
    n_0: int = 7

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = -2.87939

    assert obs == approx(exp, abs=tol)


def test_secant_method_trig_2() -> None:
    def f(x: float) -> float:
        return x - math.cos(x)

    p_0: float = 0.0
    p_1: float = 1.57080
    tol: float = 1e-5
    n_0: int = 6

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = 0.73909

    assert obs == approx(exp, abs=tol)


def test_secant_method_trig_3() -> None:
    def f(x: float) -> float:
        return x - 0.8 - 0.2 * math.sin(x)

    p_0: float = 0.0
    p_1: float = 1.57080
    tol: float = 1e-5
    n_0: int = 5

    obs = secant_method(f, p_0, p_1, tol, n_0)
    exp: float = 0.96433

    assert obs == approx(exp, abs=tol)
