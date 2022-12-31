#!/usr/bin/env python3
from inspect import cleandoc
from collections.abc import Callable
from typing import TextIO


def newtons_method(
        function: Callable[[float], float], derivative: Callable[[float], float],
        p_0: float, tol: float, n_0: int, file: TextIO = None,
        table_output: bool = False
) -> float:
    """To find a solution to f(x) = 0 given an initial approximation p_0:
    INPUT initial approximation p_0; tolerance TOL; maximum number of iterations N0.
    OUTPUT approximate solution p or message of failure.
    """
    if table_output:
        # output table heading
        output_string = f"{'-' * 37}\nn\t\tP\n{'-' * 37}"
        if not file:
            print(output_string)
        else:
            file.write(output_string + '\n')
        row_output(0, p_0, file)

    # STEP 1: set i = 1
    i: int = 1
    f_0: float = function(p_0)

    # STEP 2: while i <= N_0 do steps 3-6
    while i <= n_0:
        # STEP 3: Compute p_i
        try:
            fp_0 = derivative(p_0)
            d = f_0 / fp_0

            # STEP 6: update p_0
            p_0 = p_0 - d
            f_0 = function(p_0)
        except ZeroDivisionError as e:
            print(e)
            return None

        if table_output:
            row_output(i, p_0, file)

        # STEP 4: if p - p0 < TOL then the procedure was successful
        if abs(d) < tol:
            output_string = cleandoc("""\
                Approximate solution P = {:.10f}
                f(P) = {:.10f}
                Number of iterations = {}
                TOL = {}
                """).format(p_0, f_0, i, tol)
            if table_output:
                output_string = '-' * 37 + '\n' + output_string
            if not file:
                print(output_string)
            else:
                file.write(output_string)
            return p_0

        # STEP 5: increment iterator
        i += 1

    # STEP 7: The procedure was unsuccessful
    output_string = cleandoc("""\
          Iteration number {} gave approximation {:.10f}, 
          with f(P) = {:.10f} not within tolerance {}.
          """.format(i, p_0, f_0, tol))
    if table_output:
        output_string = '-' * 37 + '\n' + output_string
    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return p_0


def row_output(n: int, p: float, file: TextIO) -> None:
    """Function to output row of table."""
    string = "{}\t\t{:.10f}\n".format(n, p)
    if not file:
        print(string)
    else:
        file.write(string)
