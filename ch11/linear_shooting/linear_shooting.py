#!/usr/bin/env python3
import math
from collections.abc import Callable
from typing import TextIO

LONG_BORDER = 132
SHORT_BORDER = 84


def adams_variable_step(
    function: Callable[[float, ...], float],
    a: float,
    b: float,
    alpha: float,
    tol: float,
    hmax: float,
    hmin: float,
    file: TextIO = None,
    solution: Callable[[float], float] = None,
) -> list[float]:
    """To approximate the solution of the initial-value problem y' = f(t, y),
    a <= t <= b, y(a) = alpha, with local truncation error within a given tolerance.
    INPUT endpoints a, b; initial condition alpha; tolerance TOL; maximum step size
    hmax; minimum step size hmin.
    OUTPUT i, t_i, w_i, h, where at the ith step w_i approximates y(t_i) and
    the step size h was used, or a message that the minimum step size was exceeded.
    """
    # output table heading
    if solution:
        output_string = f"{'-' * LONG_BORDER}\nt_i\t\t\ty_i=y(t_i)\t\tw_i\t\t\th\t\t\t"
        output_string += f"sigma_i\t\t\t|y_i - w_i|\n{'-' * LONG_BORDER}"
    else:
        output_string = f"{'-' * SHORT_BORDER}\nt_i\t\t\tw_i\t\t\th\t\t\tsigma_i\n{'-' * SHORT_BORDER}"
    if not file:
        print(output_string)
    else:
        file.write(output_string + "\n")

    # STEP 2:
    max_len = math.ceil(abs(b - a) / hmin)
    t = [a] + max_len * [0.0]
    w = [alpha] + max_len * [0.0]
    h = hmax
    flag = True  # FLAG will be used to exit the loop in STEP 4
    last = False  # LAST will indicate when the last value is calculated

    # output row
    row_output(t[0], w[0], 0.0, 0.0, file=file, solution=solution)

    # STEP 3: Calculate Runge-Kutta approximations
    w, t = rk4(function, 1, h, w, t)
    nflag = True  # Indicates computation from RK4
    i = 4
    t_next = t[3] + h

    # STEP 4: While (FLAG = 1) do Steps 5-20
    while flag and (not isinstance(w[j], complex) for j in range(len(w))):
        # STEP 5: Predict w_i, correct w_i
        try:
            w_p = w[i - 1] + (h / 24.0) * (
                55.0 * function(t[i - 1], w[i - 1])
                - 59.0 * function(t[i - 2], w[i - 2])
                + 37.0 * function(t[i - 3], w[i - 3])
                - 9.0 * function(t[i - 4], w[i - 4])
            )
            w_c = w[i - 1] + (h / 24.0) * (
                9.0 * function(t_next, w_p)
                + 19.0 * function(t[i - 1], w[i - 1])
                - 5.0 * function(t[i - 2], w[i - 2])
                + function(t[i - 3], w[i - 3])
            )
            sigma = 19.0 * (abs(w_c - w_p) / (270.0 * h))

            # STEP 6: If sigma <= TOL then do Steps 7-16 (result accepted)
            #           else do Steps 17-19 (result rejected)
            if sigma <= tol:
                # STEP 7: Result accepted
                w[i] = w_c
                t[i] = t_next

                # STEP 8:
                if nflag:  # Previous results also accepted
                    for j in range(i - 3, i + 1):
                        row_output(t[j], w[j], h, sigma, file=file, solution=solution)
                else:  # Previous results already accepted
                    row_output(t[i], w[i], h, sigma, file=file, solution=solution)

                # STEP 9:
                if last:
                    flag = False  # Next step is 20
                else:
                    # STEP 10:
                    i = i + 1
                    nflag = False

                    # STEP 11: Increase h if it is more accurate than required or
                    #           decrease h to include b as a mesh point
                    if sigma <= 0.1 * tol or t[i - 1] + h > b:
                        # STEP 12:
                        q = (tol / (2.0 * sigma)) ** (0.25)

                        # STEP 13:
                        if q > 4.0:
                            h = 4.0 * h
                        else:
                            h = q * h

                        # STEP 14:
                        if h > hmax:
                            h = hmax

                        # STEP 15:
                        if t[i - 1] + 4.0 * h > b:
                            h = (b - t[i - 1]) / 4.0
                            last = True

                        # STEP 16:
                        w, t = rk4(function, i, h, w, t)
                        nflag = 1
                        i = i + 3  # True branch completed. End Step 6. Next step is 20

            else:
                # STEP 17: Flase branch from Step 6: result rejected
                q = (tol / (2.0 * sigma)) ** (0.25)

                # STEP 18:
                if q < 0.1:
                    h = 0.1 * h
                else:
                    h = q * h

                # STEP 19:
                if h < hmin:
                    flag = False
                    raise ArithmeticError(
                        "Minimum h exceeded, procedure completed unsuccessfully."
                    )
                else:
                    if nflag:  # Previous results also rejected
                        i = i - 3
                    w, t = rk4(function, i, h, w, t)
                    i = i + 3
                    nflag = True  # End Step 6

        except ZeroDivisionError as e:
            print(e)
            return []

        # STEP 20: End Step 4
        t_next = t[i - 1] + h

    # STEP 21: stop
    if solution:
        output_string = "-" * LONG_BORDER + "\n"
    else:
        output_string = "-" * SHORT_BORDER + "\n"

    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return w[0 : i + 2]


def rk4(
    function: Callable[[float, ...], float],
    i: int,
    h: float,
    v: list[float],
    x: list[float],
) -> tuple[list[float]]:
    # STEP 1: Return {(x_j, v_j)| j = 1, 2, 3}
    for j in range(i, i + 3):
        k_1 = h * function(x[j - 1], v[j - 1])
        k_2 = h * function(x[j - 1] + h / 2.0, v[j - 1] + k_1 / 2.0)
        k_3 = h * function(x[j - 1] + h / 2.0, v[j - 1] + k_2 / 2.0)
        k_4 = h * function(x[j - 1] + h, v[j - 1] + k_3)
        v[j] = v[j - 1] + (k_1 + 2.0 * k_2 + 2.0 * k_3 + k_4) / 6.0
        x[j] = x[0] + j * h

    return (v, x)


def row_output(
    t_i: float,
    w_i: float,
    h: float = 0.0,
    sigma: float = 0.0,
    file: TextIO = None,
    solution: Callable[[float], float] = None,
) -> None:
    """Function to output row of table."""
    if solution:
        output = (
            "{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}".format(
                t_i, solution(t_i), w_i, h, sigma, abs(solution(t_i) - w_i)
            )
        )
    else:
        output = "{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}".format(t_i, w_i, h, sigma)

    if not file:
        print(output)
    else:
        file.write(output + "\n")
