#!/usr/bin/env python3
from inspect import cleandoc
from collections.abc import Callable
from typing import TextIO
import pdb


class Bisection:
    """To find a solution to f(x) = 0 given the continuous function f on the interval 
    [a, b], where f(a) and f(b) have opposite signs:
    INPUT endpoints a, b; tolerance tol; maximum number of iterations n_0.
    OUTPUT approximate solution p or message of failure.
    """

    def __init__(self, function: Callable[[float], float]):
        self.function = function

    def bisect(self, a: float, b: float, tol: float, n_0: float,
               table_output: bool = False, file: TextIO = None) -> float:
        """Input endpoints a and b, tolerance tol, and maximum number of iterations
        n_0, as well as optional output file.
        """
        if table_output:
            # output table heading
            output_string = f"{'-'*80}\n\t\ta\t\tb\t\tP\t\tf(P)\n{'-'*80}"
            if not file:
                print(output_string)
            else:
                file.write(output_string)

        # STEP 1: set iterator
        i: int = 1
        f_a: float = self.function(a)
        p: float = 0.0
        f_p: float = 0.0

        # STEP 2: while i < N0 do steps 3-6
        while i <= n_0:
            pdb.set_trace()
            # STEP 3: compute p_i
            c: float = (b - a) / 2.0
            p = a + c
            f_p = self.function(p)

            # if table output selected, output row
            if table_output:
                self._row_output(i, a, b, p, f_p, file)

            # STEP 4: procedure completed successfully
            if abs(f_p) == 0.0 or c < tol:
                output_string = cleandoc("""\
                    Approximate solution P = {:.10f}
                    f(P) = {:.10}
                    Number of iterations = {}
                    TOL = {}
                    """.format(p, f_p, i, tol))
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
                b = p   # f(a) is unchanged

        # STEP 7: method failed, output result
        output_string = cleandoc("""\
            Method failed after {} iterations with approximation {:.10f}
            and f(P) = {:.10f} not within tolerance {}.
            """.format(n_0, p, f_p, tol))
        if not file:
            print(output_string)
        else:
            file.write(output_string)
            file.close()

    @staticmethod
    def _row_output(n: int, a: float, b: float, p: float, f_p: float,
                    file: TextIO) -> None:
        """Function to output row of table."""
        string = "{}\t\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, a, b, p, f_p)
        if not file:
            print(string)
        else:
            file.write(string)
