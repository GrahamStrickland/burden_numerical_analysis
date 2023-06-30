#!/usr/bin/env python3
from typing import TextIO

import numpy as np


def pade_rational_approximation(
        m: int, n: int, maclaurin_coeffs: list[float], file: TextIO = None
) -> list[list[float]]:
    """To obtain the rational approximation r(x) = p(x)/q(x) 
    = sum_i=0^n p_ix^i / sum_j=0^m q_j x^j for a given function f(x):
    INPUT nonnegative integers m and n.
    OUTPUT coefficients q_0, q_1, ..., q_m and p_0, p_1, ..., p_n."""

    # STEP 1
    max_degree = m + n
    b = np.zeros((max_degree, max_degree+1)) 
    q = np.zeros(m)
    p = np.zeros(n)

    # STEP 2, 3: Maclaurin coefficients were input.
    q[0] = 1.
    p[0] = maclaurin_coeffs[0]

    # STEP 4: Set up a linear system with matrix B.
    for i in range(max_degree):
        # STEP 5
        for j in range(i):
            if j < n:
                b[i][j] = 0.

        # STEP 6
        if i < n:
            b[i][i] = 1.

        # STEP 7
        for j in range(i+1, max_degree):
            b[i][j] = 0.

        # STEP 8
        for j in range(i+1):
            if j < m:
                b[i][n+j] = -maclaurin_coeffs[i-j-1]

        # STEP 9
        for j in range(n+i+1, max_degree):
            b[i][j] = 0.

        # STEP 10
        b[i][max_degree] = maclaurin_coeffs[i]

    # Steps 11-22 solve the linear system using partial pivoting.
    # STEP 11
    for i in range(n, max_degree-1):
        # STEP 12: Find pivot element.
        k = 0
        max_element = 0
        for j in range(i, max_degree):
            if abs(b[j][i]) > max_element:
                max_element = b[j][i]
        for pivot in range(i, max_degree):
            if abs(b[pivot][i]) == abs(max_element):
                k = pivot
                break

        # STEP 13: STOP.
        if b[k][i] == 0.:
            if not file:
                print("The system is singular.")
            else:
                file.write("The system is singular.")
            return []

        # STEP 14: Interchange row i and row k.
        if k != i:
            for j in range(i, max_degree+1):
                b[i][j], b[k][j] = b[k][j], b[i][j]

        # STEP 15: Perform elimination.
        for j in range(i+1, max_degree):
            # STEP 16
            try:
                xm = b[j][i] / b[i][i]
            except ZeroDivisionError as e:
                print(e)
                return []

            # STEP 17
            for k in range(i+1, max_degree+1):
                b[j][k] = b[j][k] - xm*b[i][k]

            # STEP 18
            b[j][i] = 0.

    # STEP 19: STOP.
    if b[max_degree-1][max_degree-1] == 0.:
        if not file:
            print("The system is singular.")
        else:
            file.write("The system is singular.")
        return []

    # STEP 20: Start backward substitution.
    if m > 0:
        try:
            q[m-1] = b[max_degree-1][max_degree] / b[max_degree-1][max_degree-1]
        except ZeroDivisionError as e:
            print(e)
            return []

    # STEP 21
    for i in range(max_degree-2, n-1, -1):
        sum = 0
        for j in range(i+1, max_degree):
            sum += b[i][j] * q[j-n]
        try:
            q[i-n] = b[i][max_degree] - (sum/b[i][i]) 
        except ZeroDivisionError as e:
            print(e)
            return []

    # STEP 22
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(n, max_degree):
            sum += b[i][j] * q[j-n] 
        p[i] = b[i][max_degree] - sum 

    # STEP 23: The procedure was successful.
    if not file:
        print(f"q = {q}")
        print(f"p = {p}")
    else:
        file.write(q)
        file.write(p)

    return [q.tolist(), p.tolist()]
