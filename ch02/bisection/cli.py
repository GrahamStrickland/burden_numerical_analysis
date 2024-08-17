#!/usr/bin/env python3
import argparse
import math
from typing import Callable, TextIO

from bisection import bisect


def predefined_function(x: float) -> float:
    """Predefined function in case user does not define a function."""
    return x - math.exp(x)


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the endpoints, tolerance, and maximum number of inputs supplied in a CSV file."""
    vals = input_file.read().split(",")
    a: float = float(vals[0])
    b: float = float(vals[1])
    tol: float = float(vals[2])
    n_0: int = int(vals[3])

    return {"a": a, "b": b, "tol": tol, "n_0": n_0}


def check_input_params(
    f: Callable[[float], float], a: float, b: float, tol: float, n_0: int
) -> None:
    """Check that the endpoints are not the same, the function values at the
    endpoints f(a) and f(b) have opposite signs, the tolerance is positive,
    and the number of iterations is positive.
    """
    # check that b != a
    if b == a:
        raise IOError("a and b cannot have the same value.")

    # if b < a then reverse order of a and b
    if b < a:
        a, b = b, a

    # define f(a) and f(b)
    f_a: float = f(a)
    f_b: float = f(b)

    # check that f(a) and f(b) have different signs
    if f_a * f_b > 0.0:
        raise IOError("f(a) and f(b) cannot have the same sign.")

    # check that TOL > 0
    if tol <= 0.0:
        raise IOError("Tolerance must be a positive number.")

    # check that n_0 > 0
    if n_0 <= 0:
        raise IOError("Maximum number of iterations must be a positive integer.")


def main():
    parser = argparse.ArgumentParser(description=bisect.__doc__)

    parser.add_argument(
        "a",
        nargs="?",
        default=None,
        type=float,
        help="The left endpoint of the interval.",
    )
    parser.add_argument(
        "b",
        nargs="?",
        default=None,
        type=float,
        help="The right endpoint of the interval.",
    )
    parser.add_argument(
        "--function",
        nargs="?",
        default=None,
        type=str,
        help="A function continuous on the endpoints a and b.",
    )
    parser.add_argument(
        "--tol",
        nargs="?",
        default=1e-6,
        type=float,
        help="The tolerance for the function.",
    )
    parser.add_argument(
        "--n_0",
        nargs="?",
        default=100,
        type=int,
        help="The maximum number of iterations.",
    )
    parser.add_argument(
        "--input_file",
        nargs="?",
        default=None,
        type=argparse.FileType("r"),
        help="The name of the input file.",
    )
    parser.add_argument(
        "--output_file",
        nargs="?",
        default=None,
        type=argparse.FileType("w"),
        help="The name of the output file.",
    )
    parser.add_argument(
        "--table_output", action="store_true", help="Flag for table output."
    )

    args = parser.parse_args()

    if args.function:
        function = lambda x: eval(args.function)
    else:
        function = predefined_function

    if args.input_file:
        if args.a or args.b:
            raise IOError(
                "If an input file has been defined, no other input parameters must be defined."
            )
        params = parse_file_input(args.input_file)
        a, b, tol, n_0 = params["a"], params["b"], params["tol"], params["n_0"]
    else:
        if args.a is None or args.b is None:
            raise IOError(
                "If an input file has not been defined, the endpoints must be specified as arguments."
            )
        a, b, tol, n_0 = args.a, args.b, args.tol, args.n_0

    check_input_params(function, a, b, tol, n_0)

    if args.output_file:
        args.output_file.write("This is the Bisection Algorithm.\n")
        _ = bisect(
            function=function,
            a=a,
            b=b,
            tol=tol,
            n_0=n_0,
            file=args.output_file,
            table_output=True,
        )
        args.output_file.close()
    else:
        print("This is the Bisection Algorithm.")
        _ = bisect(
            function=function,
            a=a,
            b=b,
            tol=tol,
            n_0=n_0,
            file=None,
            table_output=args.table_output,
        )


if __name__ == "__main__":
    main()
