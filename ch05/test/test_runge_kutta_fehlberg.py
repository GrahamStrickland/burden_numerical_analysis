#!/usr/bin/env python3
import math
from pytest import approx

from ..runge_kutta_fehlberg.runge_kutta_fehlberg import runge_kutta_fehlberg


def test_runge_kutta_fehlberg() -> None:
    def func(t: float, y: float) -> float:
        return y - t**2 + 1.0

    a = .0
    b = 2.
    alpha = .5
    tol = 1e-5
    hmax = .25
    hmin = .01

    obs = runge_kutta_fehlberg(
        function=func, a=a, b=b, alpha=alpha, tol=tol, hmax=hmax, hmin=hmin
        )
    exp = [.5000000, .9204886, 1.3964910, 1.9537488, 2.5864260, 3.2604605, 
           3.9520955, 4.6308268, 5.2574861, 5.3054896] 

    assert obs == approx(exp, abs=tol)
