#!/usr/bin/env python3
import math
from pytest import approx

from ..modified_eulers_method.modified_eulers_method import modified_eulers_method


def test_modified_eulers_method() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = 0.
    b = 2.
    alpha = .5
    n = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [0.5000000, 0.8260000, 1.2069200, 1.6372424, 2.1102357, 2.6176876,
           3.1495789, 3.6936862, 4.2350972, 4.7556185, 5.2330546]

    assert obs == approx(exp, abs=1e-7)


def test_modified_eulers_method2() -> None:
    def func(t: float, y: float) -> float:
        return t*math.exp(3.*t) - 2.*y

    a = 0.
    b = 1.
    alpha = 0.
    n = 2

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 0.5602111, 5.3014898]

    assert obs == approx(exp, abs=1e-7)


def test_modified_eulers_method3() -> None:
    def func(t: float, y: float) -> float:
        return 1. + (t-y)**2

    a = 2.
    b = 3.
    alpha = 1.
    n = 2

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.8125, 2.4815531]


    assert obs == approx(exp, abs=1e-7)


def test_modified_eulers_method4() -> None:
    def func(t: float, y: float) -> float:
        return 1. + (y/t)

    a = 1.
    b = 2.
    alpha = 2.
    n = 4

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 2.775, 3.6008333, 4.4688294, 5.3728586]

    assert obs == approx(exp, abs=1e-7)


def test_modified_eulers_method5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.*t) + math.sin(3.*t)

    a = 0.
    b = 1.
    alpha = 1.
    n = 4

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [alpha, 1.3199027, 1.70703, 2.005356, 2.0770789]

    assert obs == approx(exp, abs=1e-7)


def test_modified_eulers_method6() -> None:
    def func(t: float, y: float) -> float:
        return y/t - (y/t)**2

    a = 1.
    b = 2.
    alpha = 1.
    n = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [1.0147137, 1.0669093, 1.1102751, 1.1808345]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)


def test_modified_eulers_method7() -> None:
    def func(t: float, y: float) -> float:
        return 1. + y/t + (y/t)**2

    a = 1.
    b = 3.
    alpha = 0.
    n = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [.4850495, 1.6384229, 2.8250651, 5.7075699]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)

def test_modified_eulers_method8() -> None:
    def func(t: float, y: float) -> float:
        return -(y+1.)*(y+3.)

    a = 0.
    b = 2.
    alpha = -2.
    n = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [-1.6229206, -1.2442903, -1.1200763, -1.0391938]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)

def test_modified_eulers_method9() -> None:
    def func(t: float, y: float) -> float:
        return -5.*y + 5.*t**2 + 2.*t

    a = 0.
    b = 1.
    alpha = 1./3.
    n = 10

    obs = modified_eulers_method(function=func, a=a, b=b, alpha=alpha, n=n)
    exp = [.1742708, .28782, .5088359, 1.0096377]

    assert obs[2] == approx(exp[0], abs=1e-7)
    assert obs[5] == approx(exp[1], abs=1e-7)
    assert obs[7] == approx(exp[2], abs=1e-7)
    assert obs[10] == approx(exp[3], abs=1e-7)
