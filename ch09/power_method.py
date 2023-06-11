#!/usr/bin/env python3
import numpy as np


def power_method(
        n: int, A: np.array, x: np.array, tol: float, max_num: int
) -> tuple[float, np.array]:
    """To approximate the dominant eigenvalue and associated eigenvector of the 
    n x n matrix A given a nonzero vector x:
    INPUT dimension n; matrix A; vector x; tolerance TOL; maximum number 
    of iterations N.
    OUTPUT approximate eigenvalue mu; approximate eigenvector x 
    (with ||x||_infty = 1)
    or a message that the maximum number of iterations was exceeded
    """
    mu = 0.
    err = .0

    # STEP 1
    k = 0

    # STEP 2: Find the smallest integer p with 1 <= p <= n 
    #         and |x_p| = ||x||_inf.
    p = 0
    for i in range(len(x)):
        if abs(x[i]) == max(abs(x)):
            p = i
            break

    # STEP 3
    try:
        x = x / x[p]
    except ZeroDivisionError as e:
        print(e)
        return (mu, x)

    # STEP 4: While (k <= N) do Steps 5-11.
    while k < max_num:
        # STEP 5: Set y = Ax.
        y = A @ x

        # STEP 6
        mu = y[p]

        # STEP 7: Find the smallest integer p with 1 <= p <= n 
        #         and |y_p| = ||y||_inf.
        p = 0
        for i in range(n):
            if abs(y[i]) == max(abs(y)):
                p = i
                break

        # STEP 8
        if y[p] == 0.:
            print(f"Eigenvector {x}")
            print("A has the eigenvalue 0, select new vector x and restart.")
            return (mu, x)

        # STEP 9: Set ERR = ||x - (y/y)_p)||_inf;
        #                     x = y/y_p.
        err = max(abs(x - (y/y[p])))
        x = y / y[p]

        # STEP 10
        if err < tol:
            print(f"The procedure was successful after {k} iterations.")
            return (mu, x)
    
        # STEP 11
        k = k + 1

    # STEP 12: OUTPUT('The maximum number of iterations exceeded');
    #                (The procedure was successful.)
    #          STOP.
    print("The maximum number of iterations exceeded.")
    return (mu, x)


def main():
    n = 3
    A = np.array([[2., 0., 1.],
                  [-22., -3., 10.],
                  [-12., 0., 9.]])
    x = np.array([1., 1., 1.])
    tol = 1e-9
    N = 200

    (mu, x) = power_method(n, A, x, tol, N)

    print("Result: mu = {:.7f}, x = {}".format(mu, x))


if __name__ == "__main__":
    main()
