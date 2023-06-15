#!/usr/bin/env python3
import math

from sympy import Function, Symbol, factorial 

from collections.abc import Callable
from typing import TextIO


def pade_rational_approximation(
        function: Callable, m: int, n: int, 
        maclaurin_coeffs: list[float] = None, file: TextIO = None
) -> list[list[float]]:
    """To obtain the rational approximation r(x) = p(x)/q(x) 
    = sum_i=0^n p_ix^i / sum_j=0^m q_j x^j for a given function f(x):
    INPUT nonnegative integers m and n.
    OUTPUT coefficients q_0, q_1, ..., q_m and p_0, p_1, ..., p_n."""

    # STEP 1: Set N = m + n.
    max_degree = m + n

    # STEP 2: For i = 0, 1, ..., N set a_i = f^(i)(0)/i!.
    #         (The coefficients of the Maclaurin polynomial are a_0, ..., a_N,
    #         which could be input instead of calculated.)
    a = get_maclaurin_coeffs(max_degree, function)
    print(a)

    # STEP 3: Set q_0 = 1;
    #             p_0 = a_0.

    # STEP 4: For i = 1, 2, ..., N do Steps 5-10. (Set up a linear system with 
    #         matrix B.)

        # STEP 5: For j = 1, 2, ..., i - 1
        #           if j <= n then set b_i,j = 0.

        # STEP 6: If i <= n then set b_i,i = 1.

        # STEP 7: For j = i+1, i+2, ..., N set b_i,j = 0.

        # STEP 8: For j = 1, 2, ..., i
        #           if j <= m then set b_i,n+j = -a_i-j.

        # STEP 9: For j = n+i+1, n+i+2, ..., N set b_i,j = 0.

        # STEP 10: Set b_i,N+1 = a_i.

    # (Steps 11-22 solve the linear system using partial pivoting.)
    # STEP 11: For i = n+1, n+2, ..., N-1 do Steps 12-18.

        # STEP 12: Let k be the smallest integer with i <= k <= N and |b_k,i|
        #           = max_i<=j<=N |b_j,i|.
        #           (Find pivot element.)

        # STEP 13: If b_k,i = 0 then OUTPUT("The system is singular");
        #                            STOP.

        # STEP 14: If k!= i then (Interchange row i and row k.)
        #           for j = i, i+1, ..., N+1 set
        #           b_COPY = b_i,j;
        #           b_i,j = b_k,j;
        #           b_k,j = b_COPY.

        # STEP 15: For j = i+1, i+2, ..., N do Steps 16-18. (Perform elimination.)

            # STEP 16: Set xm = b_j,i / b_i,i.

            # STEP 17: For k = i+1, i+2, ..., N+1
            #           set b_j,k = b_j,k - xm*b_i,k.

            # STEP 18: Set b_j,i = 0.

    # STEP 19: If b_N,N = 0 then OUTPUT("The system is singular");
    #                            STOP.

    # STEP 20: If m > 0 then set q_m = b_N,N+1 / b_N,N. 
    #           (Start backward substitution.)

    # STEP 21: For i = N-1, N-2, ..., n+1 
    #           set q_i-n = b_i,N+1 - sum_j=i+1^N b_i,j * q_j-n / b_i,i.

    # STEP 22: For i = n, n-1, ..., 1 set p_i = b_i,N+1 - sum_j=n+1^N b_i * q_j-n.

    # STEP 23: OUTPUT(q_0, q_1, ..., q_m, p_0, p_1, ..., p_n);
    #          STOP. (The procedure was successful.)


def get_maclaurin_coeffs(n: int, function: Callable) -> list[float]:
    x = Symbol('x')
    f = Function('function')
    coeffs = []
    
    for i in range(n + 1):
        derivative = f(x).diff(x, i)
        coefficient = derivative.subs(x, 0) / factorial(i)
        coeffs.append(float(coefficient))
    
    return coeffs
