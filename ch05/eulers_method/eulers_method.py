#!/usr/bin/env python3
from collections.abc import Callable
from typing import TextIO


LONG_BORDER = 76
SHORT_BORDER = 28


def eulers_method(
        function: Callable[[float, ...], float], a: float, b: float, alpha: float,
        n: int, file: TextIO = None, solution: Callable[[float], float] = None
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
        file.write(output_string + '\n')

    # STEP 1:
    i: int = 1
    h: float = (b - a) / n
    t: float = a
    w: float = alpha
    solutions = [w]

    # output row
    row_output(t, w, file, solution)

    # STEP 2: for i = 1, 2, ..., N do steps 3, 4
    while i <= n and not isinstance(w, complex):
        # STEP 3: compute w_i
        try:
            w = w + h * function(t, w)
            t = a + i * h
            solutions.append(w)
        except ZeroDivisionError as e:
            print(e)
            return []

        # STEP 4: output row
        row_output(t, w, file, solution)

        i += 1

    # STEP 5: stop
    if solution:
        output_string = '-' * LONG_BORDER + '\n'
    else:
        output_string = '-' * SHORT_BORDER + '\n'

    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return solutions


def row_output(
        t_i: float, w_i: float, file: TextIO, solution: Callable[[float], float] = None
) -> None:
    """Function to output row of table."""
    if solution:
        output = "{:.1f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}".format(t_i, w_i, solution(t_i), abs(solution(t_i) - w_i))
    else:
        output = "{:.1f}\t\t{:.10f}".format(t_i, w_i)

    if not file:
        print(output)
    else:
        file.write(output + '\n')
