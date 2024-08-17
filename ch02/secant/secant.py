#!/usr/bin/env python3
from inspect import cleandoc
from collections.abc import Callable
from typing import TextIO


def secant_method(
    function: Callable[[float], float],
    p_0: float,
    p_1: float,
    tol: float,
    n_0: int,
    file: TextIO = None,
    table_output: bool = False,
) -> float:
    """To find a solution to f(x) = 0 given initial approximations p_0 and p_1:
    INPUT initial approximations p_0 and p_1; tolerance TOL; maximum number of iterations N0.
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
        row_output(1, p_1, file)

    # STEP 1: set iterator and function values q0 and q1
    i: int = 2
    q_0: float = function(p_0)
    q_1: float = function(p_1)
    p: float = 0.0
    f_p: float = 0.0

    # STEP 2: while i <= N_0 do steps 3-6
    while i <= n_0:
        # STEP 3: Compute p_i
        try:
            p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
        except ZeroDivisionError as e:
            print(e)
            return None

        if table_output:
            row_output(i, p_0, file)

        # STEP 4: check if procedure was successful
        f_p = function(p)
        if abs(p - p_1) < tol:
            output_string = cleandoc("""\
                Approximate solution P = {:.10f}
                f(P) = {:.10f}
                Number of iterations = {}
                TOL = {}
                """).format(p, f_p, i, tol)
            if table_output:
                output_string = "-" * 37 + "\n" + output_string
            if not file:
                print(output_string)
            else:
                file.write(output_string)
            return p
        else:
            # STEP 5: increment iterator
            i += 1

            # STEP 6: update p_0, q_0, p_1, q_1
            p_0 = p_1
            q_0 = q_1
            p_1 = p
            q_1 = f_p

    # STEP 7: The procedure was unsuccessful
    output_string = cleandoc(
        """\
          Iteration number {} gave approximation {:.10f},
          with f(P) = {:.10f}
          not within tolerance {}.
          """.format(i, p, f_p, tol)
    )
    if table_output:
        output_string = "-" * 37 + "\n" + output_string
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
