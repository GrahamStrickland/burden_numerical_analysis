#!/usr/bin/env python3
import math
from collections.abc import Callable
from typing import TextIO


class Bisection:
    """To find a solution to f(x) = 0 given the continuous function f on the interval 
    [a, b], where f(a) and f(b) have opposite signs:
    INPUT endpoints a, b; tolerance tol; maximum number of iterations n_0.
    OUTPUT approximate solution p or message of failure.
    """

    def __init__(self, function: Callable[float]):
        self.function = function

    def bisect(self, a: float, b: float, tol: float, n_0: float,
               file=None: TextIO) -> list[float]:
        """Input endpoints a and b, tolerance tol, and maximum number of iterations
        n_0, as well as optional output file.
        """
        a = b = f_a = f_b = tol = 0.0
        n_0 = 0

        if file:
            open(file, 'w')

        # STEP 1: set iterator
        i = 1

        # STEP 2: while i < N0 do steps 3-6
        while i < n_0:
            # STEP 3: compute p_i
            c = (b - a)/2.0
            p = a + c
            f_p = f(p)

            # if table output selected, output row
            if file:
                _row_output(i, a, b, p, f_p, file)

            # STEP 4: procedure completed successfully
            if abs(f_p) < 0.0 or c < tol:
                output_string = """
                    Approximate solution P = {:.10f}
                    f(P) = {:.10}
                    Number of iterations = {}
                    TOL = {}
                    """.format(p, f_p, i, TOL)
                print(output_string)
            return
          
            # STEP 5: increment iterator to continue running algorithm
            i += 1

            # STEP 6: compute a_i and b_i
            if f_a * f_p > 0.0:
                a = p
                f_a = f_p
            else:
                b = p # f(a) is unchanged
                f_b = f_p

        # STEP 7: method failed, output result
        output_string = """
            Iteration number {} gave approximation {:.10f}, 
            with f(P) = {:.10f} not within tolerance {}.
            """.format(n_0, p, f_p, tol))
        file.write(output_string)
        file.close()


    def _row_output(self, n: int, a: float, b: float, p: float, f_p: float, 
                    file: TextIO) -> None:
        """Function to output row of table."""
        string = "{}\t\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, a, b, p, f_p())
        file.write(string)
