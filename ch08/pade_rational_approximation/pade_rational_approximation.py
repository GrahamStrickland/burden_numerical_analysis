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

    # STEP 1: Set N = m + n.
    max_degree = m + n
    b = np.zeros((max_degree, max_degree+1)) 
    q = np.zeros(m+1)
    p = np.zeros(n+1)

    # STEP 2: For i = 0, 1, ..., N set a_i = f^(i)(0)/i!.
    #         (The coefficients of the Maclaurin polynomial are a_0, ..., a_N,
    #         which could be input instead of calculated.)

    # STEP 3: Set q_0 = 1;
    #             p_0 = a_0.
    q[0] = 1.
    p[0] = maclaurin_coeffs[0]

    # STEP 4: For i = 1, 2, ..., N do Steps 5-10. (Set up a linear system with 
    #         matrix B.)
    for i in range(max_degree):
        # STEP 5: For j = 1, 2, ..., i - 1
        #           if j <= n then set b_i,j = 0.
        for j in range(i):
            if j < n:
                b[i][j] = 0.

        # STEP 6: If i <= n then set b_i,i = 1.
        if i < n:
            b[i][i] = 1.

        # STEP 7: For j = i+1, i+2, ..., N set b_i,j = 0.
        for j in range(i+1, max_degree):
            b[i][j] = 0.

        # STEP 8: For j = 1, 2, ..., i
        #           if j <= m then set b_i,n+j = -a_i-j.
        for j in range(i+1):
            if j < m:
                b[i][n+j] = -maclaurin_coeffs[i-j]

        # STEP 9: For j = n+i+1, n+i+2, ..., N set b_i,j = 0.
        for j in range(n+i+1, max_degree):
            b[i][j] = 0.

        # STEP 10: Set b_i,N+1 = a_i.
        b[i][max_degree] = maclaurin_coeffs[i]

    # (Steps 11-22 solve the linear system using partial pivoting.)
    # STEP 11: For i = n+1, n+2, ..., N-1 do Steps 12-18.
    for i in range(n, max_degree-1):
        # STEP 12: Let k be the smallest integer with i <= k <= N and |b_k,i|
        #           = max_i<=j<=N |b_j,i|.
        #           (Find pivot element.)
        k = 0
        max_element = 0
        for j in range(i, max_degree):
            if abs(b[j][i]) > max_element:
                max_element = b[j][i]
        for pivot in range(i, max_degree):
            if abs(b[pivot][i]) == abs(max_element):
                k = pivot
                break

        # STEP 13: If b_k,i = 0 then OUTPUT("The system is singular");
        #                            STOP.
        if b[k][i] == 0.:
            if not file:
                print("The system is singular.")
            else:
                file.write("The system is singular.")
            return []

        # STEP 14: If k!= i then (Interchange row i and row k.)
        #           for j = i, i+1, ..., N+1 set
        #           b_COPY = b_i,j;
        #           b_i,j = b_k,j;
        #           b_k,j = b_COPY.
        if k != i:
            for j in range(i, max_degree+1):
                b[i][j], b[k][j] = b[k][j], b[i][j]

        # STEP 15: For j = i+1, i+2, ..., N do Steps 16-18. (Perform elimination.)
        for j in range(i+1, max_degree):
            # STEP 16: Set xm = b_j,i / b_i,i.
            try:
                xm = b[j][i] / b[i][i]
            except ZeroDivisionError as e:
                print(e)
                return []

            # STEP 17: For k = i+1, i+2, ..., N+1
            #           set b_j,k = b_j,k - xm*b_i,k.
            for k in range(i+1, max_degree+1):
                b[j][k] = b[j][k] - xm*b[i][k]

            # STEP 18: Set b_j,i = 0.
            b[j][i] = 0.

    # STEP 19: If b_N,N = 0 then OUTPUT("The system is singular");
    #                            STOP.
    if b[max_degree-1][max_degree-1] == 0.:
        if not file:
            print("The system is singular.")
        else:
            file.write("The system is singular.")
        return []

    # STEP 20: If m > 0 then set q_m = b_N,N+1 / b_N,N. 
    #           (Start backward substitution.)
    if m > 0:
        try:
            q[m] = b[max_degree-1][max_degree] / b[max_degree-1][max_degree-1]
        except ZeroDivisionError as e:
            print(e)
            return []

    # STEP 21: For i = N-1, N-2, ..., n+1 
    #           set q_i-n = b_i,N+1 - sum_j=n+1^N b_i,j * q_j-n / b_i,i.
    for i in range(max_degree-2, n-1, -1):
        sum = 0
        for j in range(i+1, max_degree):
            sum += b[i][j] * q[j-n+1]
        try:
            q[i-n+1] = b[i][max_degree] - (sum/b[i][i]) 
        except ZeroDivisionError as e:
            print(e)
            return []

    # STEP 22: For i = n, n-1, ..., 1 set p_i = b_i,N+1 - sum_j=n+1^N b_i,j * q_j-n.
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(n, max_degree):
            sum += b[i][j] * q[j-n+1] 
        p[i] = b[i][max_degree] - sum 

    # STEP 23: OUTPUT(q_0, q_1, ..., q_m, p_0, p_1, ..., p_n);
    #          STOP. (The procedure was successful.)
    if not file:
        print(q, p)
    else:
        file.write(q)
        file.write(p)

    return [q.tolist(), p.tolist()]
