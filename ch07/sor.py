#!/usr/bin/env python3
import numpy as np


def sor(a: np.array, n: int, b: np.array, x_0: np.array, omega: float, 
        tol: float, max_iter: int
) -> np.array:
    """To solve Ax = b given the parameter omega and an initial approximation x0:
    INPUT the number of equations and unknowns n:
    the entries a[i,j], 1 <= i, j <= n of the matrix A;
    the entries b[i], 1 <= i <= n of b; the entries XO[i],
    of XO = x0; the parameter omega; tolerance TOL;
    maximum number of iterations N.
    OUTPUT the approximate solution x[1],...,x[n] or a message that the
    number of iterations was exceeded.
    """
    x = np.zeros(n)

    print("This is the SOR Method for Linear Systems.")

    # STEP 1
    k = 1

    # STEP 2
    while k <= max_iter:
        # STEP 3
        for i in range(n):
            sum_1 = 0.
            sum_2 = 0.
            for j in range(i):
                sum_1 += a[i,j] * x[j]
            for l in range(i+1, n):
                sum_2 += a[i,l] * x_0[l]
            x[i] = ((1.-omega) * x_0[i]) + (omega * (-sum_1-sum_2+b[i])) / a[i,i]

        # STEP 4: If ||x - XO|| < TOL then procedure was successful.
        norm = abs(x[0] - x_0[0])
        for i in range(n):
            if abs(x[i] - x_0[i]) > norm:
                norm = abs(x[i] - x_0[i])
        if norm < tol:
            print(f"The procedure was successful after {k} iterations.")
            print(f"||x - x0|| = {norm}, < TOL = {tol}")
            return x

        # STEP 5
        k = k + 1

        # STEP 6: For i = 1,...,n set XO[i] = x[i].
        for i in range(n):
            x_0[i] = x[i]

    # STEP 7
    print("The procedure was not successful.")


def main() -> None:
    a = np.array([[3., -1., 1.],
                  [3., 6., 2.],
                  [3., 3., 7.]])
    n = 3
    b = np.array([1., 0., 4.])
    x_0 = np.array([0., 0., 0.])
    omega = 1.2
    tol = 1e-3
    max_iter = 200

    x = sor(a, n, b, x_0, omega, tol, max_iter)

    print(f"Result: x = {x}")


if __name__ == "__main__":
    main()
