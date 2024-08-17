#!/usr/bin/env python3
from inspect import cleandoc
from collections.abc import Callable
from typing import TextIO


def fixed_point(
    function: Callable[[float], float],
    p_0: float,
    tol: float,
    n_0: int,
    file: TextIO = None,
    table_output: bool = False,
) -> float:
    """To find a solution to p = g(p) given an initial approximation p_0:
    INPUT initial approximation p_0; tolerance TOL; maximum number of iterations n_0.
    OUTPUT approximate solution p or message of failure.
    """
    if table_output:
        # output table heading
        output_string = f"{'-' * 37}\nn\t\tP\n{'-' * 37}"
        if not file:
            print(output_string)
        else:
            file.write(output_string + "\n")
        row_output(0, p_0, file)

    # STEP 1: set iterator
    i: int = 1
    p: float = 0.0

    # STEP 2: do Steps 3-6
    while i <= n_0 and not isinstance(p, complex):
        # STEP 3: compute p_i
        try:
            p = function(p_0)
        except ZeroDivisionError as e:
            print(e)
            return None

        if table_output:
            row_output(i, p, file)

        # STEP 4: the procedure was successful
        if abs(p - p_0) < tol:
            output_string = cleandoc("""\
            Approximate solution P = {:.10f}
            Number of iterations = {}
            TOL = {}
            """).format(p, i, tol)
            if table_output:
                output_string = "-" * 37 + "\n" + output_string
            if not file:
                print(output_string)
            else:
                file.write(output_string)
            return p

        # STEP 5: increment iterator
        i += 1

        # STEP 6: update p_0
        p_0 = p

    # STEP 7: the procedure was unsuccessful
    output_string = cleandoc(
        """\
        The method failed after {} iterations,
        gave approximation {:.10f}, 
        not within tolerance {}.
        """.format(i, p, tol)
    )
    if table_output:
        output_string = "-" * 27 + "\n" + output_string
    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return p


def row_output(n: int, p: float, file: TextIO) -> None:
    """Function to output row of table."""
    string = "{}\t\t{:.10f}\n".format(n, p)
    if not file:
        print(string)
    else:
        file.write(string)
