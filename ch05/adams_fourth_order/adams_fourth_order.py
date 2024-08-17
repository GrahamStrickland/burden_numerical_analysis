#!/usr/bin/env python3
from collections.abc import Callable
from typing import TextIO


LONG_BORDER = 76
SHORT_BORDER = 28


def adams_fourth_order(
    function: Callable[[float, ...], float],
    a: float,
    b: float,
    alpha: float,
    n: int,
    file: TextIO = None,
    solution: Callable[[float], float] = None,
) -> list[float]:
    """To approximate the solution of the initial-value problem y' = f(t, y),
    a <= t <= b, y(a) = alpha, at (N+1) equally spaced numbers in the interval [a, b]:
    INPUT endpoints a, b; integer N; initial condition alpha.
    OUTPUT approximation w to y at the (N+1) values of t.
    """
    # output table heading
    if solution:
        output_string = f"{'-'*LONG_BORDER}\nt_i\t\tw_i\t\t\ty_i=y(t_i)\t\t|y_i - w_i|\n{'-'*LONG_BORDER}"
    else:
        output_string = f"{'-'*SHORT_BORDER}\nt_i\t\tw_i\n{'-'*SHORT_BORDER}"

    if not file:
        print(output_string)
    else:
        file.write(output_string + "\n")

    # STEP 1:
    i: int = 1
    h: float = (b - a) / n
    t = [a]
    w = [alpha]

    # output row
    row_output(0, t, w, file, solution)

    # STEP 2: for i = 1, 2, 3, do steps 3-5
    while i <= 3 and (not isinstance(w[j], complex) for j in range(len(w))):
        try:
            # STEP 3: compute intermediate values
            k_1 = h * function(t[i - 1], w[i - 1])
            k_2 = h * function(t[i - 1] + h / 2.0, w[i - 1] + k_1 / 2.0)
            k_3 = h * function(t[i - 1] + h / 2.0, w[i - 1] + k_2 / 2.0)
            k_4 = h * function(t[i - 1] + h, w[i - 1] + k_3)

            # STEP 4: Compute w_i, t_i
            w.append(w[i - 1] + (k_1 + 2.0 * k_2 + 2.0 * k_3 + k_4) / 6.0)
            t.append(a + i * h)

        except ZeroDivisionError as e:
            print(e)
            return []

        # STEP 5: output row
        row_output(i, t, w, file, solution)

        i += 1

    # STEP 6: for i = 4, ..., N do steps 7-10
    while i <= n and (not isinstance(w[j], complex) for j in range(len(w))):
        try:
            # STEP 7: predict w_i, correct w_i
            t.append(a + i * h)
            w.append(
                w[i - 1]
                + h
                * (
                    55 * function(t[i - 1], w[i - 1])
                    - 59 * function(t[i - 2], w[i - 2])
                    + 37 * function(t[i - 3], w[i - 3])
                    - 9 * function(t[i - 4], w[i - 4])
                )
                / 24.0
            )
            w[i] = (
                w[i - 1]
                + h
                * (
                    9 * function(t[i], w[i])
                    + 19 * function(t[i - 1], w[i - 1])
                    - 5 * function(t[i - 2], w[i - 2])
                    + function(t[i - 3], w[i - 3])
                )
                / 24.0
            )

        except ZeroDivisionError as e:
            print(e)
            return []

        # STEP 8: output row
        row_output(i, t, w, file, solution)

        # STEP 9, 10: Prepare for next iteration
        i += 1

    # STEP 11: stop
    if solution:
        output_string = "-" * LONG_BORDER + "\n"
    else:
        output_string = "-" * SHORT_BORDER + "\n"

    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return w


def row_output(
    i: int,
    t: list[float],
    w: list[float],
    file: TextIO,
    solution: Callable[[float], float] = None,
) -> None:
    """Function to output row of table."""
    if solution:
        output = "{:.1f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}".format(
            t[i], w[i], solution(t[i]), abs(solution(t[i]) - w[i])
        )
    else:
        output = "{:.1f}\t\t{:.10f}".format(t[i], w[i])

    if not file:
        print(output)
    else:
        file.write(output + "\n")
