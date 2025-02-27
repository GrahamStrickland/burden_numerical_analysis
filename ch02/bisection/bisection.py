#!/usr/bin/env python3
from collections.abc import Callable
from inspect import cleandoc
from typing import TextIO


def bisect(
    function: Callable[[float], float],
    a: float,
    b: float,
    tol: float,
    n_0: int,
    file: TextIO = None,
    table_output: bool = False,
) -> float:
    """To find a solution to f(x) = 0 given the continuous function f on the interval
    [a, b], where f(a) and f(b) have opposite signs:
    INPUT endpoints a, b; tolerance tol; maximum number of iterations n_0.
    OUTPUT approximate solution p or message of failure.
    """
    if table_output:
        # output table heading
        output_string = f"{'-' * 80}\n\t\ta\t\tb\t\tP\t\tf(P)\n{'-' * 80}"
        if not file:
            print(output_string)
        else:
            file.write(output_string + "\n")

    # STEP 1: set iterator
    i: int = 1
    f_a: float = function(a)
    p: float = 0.0
    f_p: float = 0.0

    # STEP 2: while i < n_0 do steps 3-6
    while i <= n_0 and not isinstance(f_p, complex):
        # STEP 3: compute p_i
        c: float = (b - a) / 2.0
        p = a + c
        try:
            f_p = function(p)
        except ZeroDivisionError as e:
            print(e)
            return None

        # if table output selected, output row
        if table_output:
            row_output(i, a, b, p, f_p, file)

        # STEP 4: procedure completed successfully
        if abs(f_p) == 0.0 or c < tol:
            output_string = cleandoc(
                """\
                Approximate solution P = {:.10f}
                f(P) = {:.10}
                Number of iterations = {}
                TOL = {}
                """.format(p, f_p, i, tol)
            )
            if table_output:
                output_string = "-" * 80 + "\n" + output_string
            if not file:
                print(output_string)
            else:
                file.write(output_string)
            return p

        # STEP 5: increment iterator to continue running algorithm
        i += 1

        # STEP 6: compute a_i and b_i
        if f_a * f_p > 0.0:
            a = p
            f_a = f_p
        else:
            b = p  # f(a) is unchanged

    # STEP 7: method failed, output result
    output_string = cleandoc(
        """\
        Method failed after {} iterations with approximation {:.10f}
        and f(P) = {:.10f} not within tolerance {}.
        """.format(i, p, f_p, tol)
    )
    if table_output:
        output_string = "-" * 80 + "\n" + output_string
    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return p


def row_output(n: int, a: float, b: float, p: float, f_p: float, file: TextIO) -> None:
    """Function to output row of table."""
    string = "{}\t\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, a, b, p, f_p)
    if not file:
        print(string)
    else:
        file.write(string)
