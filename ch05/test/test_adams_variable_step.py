#!/usr/bin/env python3
import math
from pytest import approx

from ..adams_variable_step.adams_variable_step import adams_variable_step


def test_adams_variable_step() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = 0.0
    b = 2.0
    alpha = 0.5
    tol = 1e-5
    hmax = 0.2
    hmin = 0.01

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [
        0.5,
        0.70480426,
        0.93320071,
        1.18390304,
        1.45544890,
        1.74617506,
        2.05419064,
        2.37734570,
        2.71319570,
        3.05896114,
        3.41148167,
        3.70412624,
        3.99667129,
        4.28661635,
        4.57118181,
        4.84727903,
        5.11147478,
        5.16092479,
        5.20975773,
        5.25794355,
        5.30545159,
    ]

    assert obs == approx(exp, abs=tol)


def test_adams_variable_step2() -> None:
    def func(t: float, y: float) -> float:
        return t * math.exp(3.0 * t) - 2.0 * y

    a = 0.0
    b = 1.0
    alpha = 0.0
    tol = 1e-4
    hmax = 0.25
    hmin = 0.025

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [0.00096891, 0.03529441, 0.50174348, 1.45544317, 3.19605697, 3.21912776]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[5] == approx(exp[1], abs=tol)
    assert obs[12] == approx(exp[2], abs=tol)
    assert obs[17] == approx(exp[3], abs=tol)
    assert obs[22] == approx(exp[4], abs=tol)
    assert obs[26] == approx(exp[5], abs=tol)


def test_adams_variable_step3() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + (t - y) ** 2

    a = 2.0
    b = 3.0
    alpha = 1.0
    tol = 1e-5
    hmax = 0.25
    hmin = 0.025

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [1.1213235, 1.55059834, 2.00923157, 2.49895243, 2.50000535]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[5] == approx(exp[1], abs=tol)
    assert obs[9] == approx(exp[2], abs=tol)
    assert obs[13] == approx(exp[3], abs=tol)
    assert obs[17] == approx(exp[4], abs=tol)


def test_adams_variable_step4() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t

    a = 1.0
    b = 2.0
    alpha = 2.0
    tol = 1e-5
    hmax = 0.25
    hmin = 0.025

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [2.18941363, 2.77892931, 4.84179835, 5.38629105]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[4] == approx(exp[1], abs=tol)
    assert obs[8] == approx(exp[2], abs=tol)
    assert obs[12] == approx(exp[3], abs=tol)


def test_adams_variable_step5() -> None:
    def func(t: float, y: float) -> float:
        return math.cos(2.0 * t) + math.sin(3.0 * t)

    a = 0.0
    b = 1.0
    alpha = 1.0
    tol = 1e-5
    hmax = 0.25
    hmin = 0.025

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [1.0681796, 1.42861668, 1.90768386, 2.08668486, 2.11800208]

    assert obs[1] == approx(exp[0], abs=tol)
    assert obs[5] == approx(exp[1], abs=tol)
    assert obs[10] == approx(exp[2], abs=tol)
    assert obs[13] == approx(exp[3], abs=tol)
    assert obs[16] == approx(exp[4], abs=tol)


def test_adams_variable_step6() -> None:
    def func(t: float, y: float) -> float:
        return y / t - (y / t) ** 2

    a = 1.0
    b = 4.0
    alpha = 1.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.02

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [
        1.00463041,
        1.03196889,
        1.08714711,
        1.18327922,
        1.34525123,
        1.529409,
        1.67623887,
    ]

    assert obs[5] == approx(exp[0], abs=tol)
    assert obs[15] == approx(exp[1], abs=tol)
    assert obs[25] == approx(exp[2], abs=tol)
    assert obs[35] == approx(exp[3], abs=tol)
    assert obs[45] == approx(exp[4], abs=tol)
    assert obs[52] == approx(exp[5], abs=tol)
    assert obs[57] == approx(exp[6], abs=tol)


def test_adams_variable_step7() -> None:
    def func(t: float, y: float) -> float:
        return 1.0 + y / t + (y / t) ** 2

    a = 1.0
    b = 3.0
    alpha = 0.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.02

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [
        0.20333499,
        0.73586642,
        1.48072467,
        2.51764797,
        3.92602442,
        5.50206466,
        5.87410206,
    ]

    assert obs[5] == approx(exp[0], abs=tol)
    assert obs[15] == approx(exp[1], abs=tol)
    assert obs[25] == approx(exp[2], abs=tol)
    assert obs[35] == approx(exp[3], abs=tol)
    assert obs[45] == approx(exp[4], abs=tol)
    assert obs[55] == approx(exp[5], abs=tol)
    assert obs[61] == approx(exp[6], abs=tol)


def test_adams_variable_step8() -> None:
    def func(t: float, y: float) -> float:
        return -(y + 1.0) * (y + 3.0)

    a = 0.0
    b = 3.0
    alpha = -2.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.02

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [-1.8330378, -1.42945306, -1.21150951, -1.0581934, -1.0133524, -1.00494507]

    assert obs[5] == approx(exp[0], abs=tol)
    assert obs[17] == approx(exp[1], abs=tol)
    assert obs[27] == approx(exp[2], abs=tol)
    assert obs[41] == approx(exp[3], abs=tol)
    assert obs[51] == approx(exp[4], abs=tol)
    assert obs[61] == approx(exp[5], abs=tol)


def test_adams_variable_step9() -> None:
    def func(t: float, y: float) -> float:
        return (t + 2.0 * t**3) * y**3 - t * y

    a = 0.0
    b = 2.0
    alpha = 1.0 / 3.0
    tol = 1e-6
    hmax = 0.5
    hmin = 0.02

    obs = adams_variable_step(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
    )
    exp = [0.32153668, 0.24281066, 0.15096743, 0.09815109, 0.06418555, 0.0543453]

    assert obs[5] == approx(exp[0], abs=tol)
    assert obs[15] == approx(exp[1], abs=tol)
    assert obs[20] == approx(exp[2], abs=tol)
    assert obs[25] == approx(exp[3], abs=tol)
    assert obs[29] == approx(exp[4], abs=tol)
    assert obs[33] == approx(exp[5], abs=tol)
