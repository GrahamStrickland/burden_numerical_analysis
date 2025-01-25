#!/usr/bin/env python3
import numpy as np
from numpy import linalg


def inverse_power_method(
    n: int, A: np.array, x: np.array, tol: float, max_num: int
) -> tuple[float, np.array]:
    """To approximate an eigenvalue and an associated eigenvector of the
    n x n matrix A given a nonzero vector x:
    INPUT dimension n; matrix A; vector x; tolerance TOL; maximum number
    of iterations N.
    OUTPUT approximate eigenvalue mu; approximate eigenvector x
    (with ||x||_infty = 1)
    or a message that the maximum number of iterations was exceeded
    """
    mu = 0.0
    err = 0.0

    # STEP 1: Set q = (x^tAx)/(x^tx).
    q = (np.transpose(x) @ A @ x) / (np.transpose(x) @ x)

    # STEP 2
    k = 0

    # STEP 3: Find the smallest integer p with 1 <= p <= n
    #         and |x_p| = ||x||_inf.
    p = 0
    for i in range(len(x)):
        if abs(x[i]) == max(abs(x)):
            p = i
            break

    # STEP 4
    try:
        x = x / x[p]
    except ZeroDivisionError as e:
        print(e)
        return (mu, x)

    # STEP 5: While (k <= N) do Steps 6-12.
    while k < max_num:
        # STEP 6: Solve the linear system (A - qI)y = x.
        B = A - q * np.eye(3)
        y = linalg.solve(B, x)

        # STEP 7: STOP.
        if y.all() == 0.0:
            print("{:.7f} is an eigenvalue.")
            return (mu, x)

        # STEP 8
        mu = y[p]

        # STEP 9: Find the smallest integer p with 1 <= p <= n
        #         and |y_p| = ||y||_inf.
        p = 0
        for i in range(n):
            if abs(y[i]) == max(abs(y)):
                p = i
                break

        # STEP 10: Set ERR = ||x - (y/y)_p)||_inf;
        #                     x = y/y_p.
        try:
            err = max(abs(x - (y / y[p])))
            x = y / y[p]
        except ZeroDivisionError as e:
            print(e)
            return (mu, x)

        # STEP 11
        if err < tol:
            mu = (1 / mu) + q
            print(f"The procedure was successful after {k} iterations.")
            return (mu, x)

        # STEP 12
        k = k + 1

    # STEP 13: STOP.
    print("The maximum number of iterations exceeded.")
    return (mu, x)


def main():
    n = 3
    A = np.array([[2.0, 0.0, 1.0], [-22.0, -3.0, 10.0], [-12.0, 0.0, 9.0]])
    x = np.array([1.0, 1.0, 1.0])
    tol = 1e-9
    N = 200

    (mu, x) = inverse_power_method(n, A, x, tol, N)

    print("Result: mu = {:.7f}, x = {}".format(mu, x))


if __name__ == "__main__":
    main()
