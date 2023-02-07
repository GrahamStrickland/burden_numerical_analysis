#!/usr/bin/env python3
from inspect import cleandoc
from collections.abc import Callable
from typing import TextIO


def eulers_method(
        function: Callable[float, float], a: float, b: float, alpha: float,
        n: int, file: TextIO = None, table_output: bool = False
) -> list[float]:
    """To approximate the soluution of the initial-value problem y' = f(t, y),
    a <= t <= b, y(a) = alpha, at (N+1) equally spaced numbers in the interval [a, b]:
    INPUT endpoints a, b; integer N; initial condition alpha.
    OUTPUT approximation w to y at the (N+1) values of t.
    """
    if table_output:
        # output table heading
        output_string = f"{'-'*80}\n\t\tt_i\t\tw_i\n{'-'*80}"
        if not file:
            print(output_string)
        else:
            file.write(output_string + '\n')

    # STEP 1:
    i: int = 1
    h: float = (b - a) / n
    t: float = a
    w: float = alpha
    solutions: list[float] = [w]

    # if table output selected, output row
    if table_output:
        row_output(t, w, file)

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

        # STEP 4: if table output selected, output row
        if table_output:
            row_output(t, w, file)

        i += 1

    # STEP 5: stop
    if table_output:
        output_string = '-' * 80 + '\n'
        if not file:
            print(output_string)
        else:
            file.write(output_string)
    return solutions


def row_output(t_i: float, w_i: float, file: TextIO) -> None:
    """Function to output row of table."""
    string = "{}\t\t{:.10f}\t".format(t_i, w_i)
    if not file:
        print(string)
    else:
        file.write(string)
