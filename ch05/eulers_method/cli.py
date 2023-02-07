#!/usr/bin/env python3
import argparse
import math
from typing import TextIO

from eulers_method import eulers_method


def predefined_function(t: float, y: float) -> float:
    """Predefined function in case user does not define a function."""
    return y - t**2 + 1


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the endpoints, tolerance, and maximum number of inputs supplied in a CSV file."""
    vals = input_file.read().split(',')
    a: float = float(vals[0])
    b: float = float(vals[1])
    alpha: float = float(vals[2])
    n: int = int(vals[3])

    return {"a": a, 'b': b, 'alpha': alpha, 'n': n}


def check_input_params(a: float, b: float, n: int) -> None:
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

    # check that n> 0
    if n <= 0:
        raise IOError("Maximum number of iterations must be a positive integer.")


def main():
    parser = argparse.ArgumentParser(description=eulers_method.__doc__)

    parser.add_argument(
        "a",
        nargs='?',
        default=None,
        type=float,
        help="The left endpoint of the interval."
    )
    parser.add_argument(
        "b",
        nargs='?',
        default=None,
        type=float,
        help="The right endpoint of the interval."
    )
    parser.add_argument(
        "--function",
        nargs='?',
        default=None,
        type=str,
        help="A function f(t,y) continuous on the interval [a, b]."
    )
    parser.add_argument(
        "--alpha",
        nargs='?',
        default=1e-6,
        type=float,
        help="The value y(a) = alpha."
    )
    parser.add_argument(
        "--n",
        nargs='?',
        default=100,
        type=int,
        help="The number of mesh points at which the solution is to be calculated."
    )
    parser.add_argument(
        "--input_file",
        nargs='?',
        default=None,
        type=argparse.FileType('r'),
        help="The name of the input file."
    )
    parser.add_argument(
        "--output_file",
        nargs='?',
        default=None,
        type=argparse.FileType('w'),
        help="The name of the output file."
    )
    parser.add_argument(
        "--table_output",
        action="store_true",
        help="Flag for table output."
    )

    args = parser.parse_args()

    if args.function:
        function = lambda t, y: eval(args.function)
    else:
        function = predefined_function

    if args.input_file:
        if args.a or args.b:
            raise IOError("If an input file has been defined, no other input parameters must be defined.")
        params = parse_file_input(args.input_file)
        a, b, alpha, n = params["a"], params["b"], params["alpha"], params["n"]
    else:
        if args.a is None or args.b is None:
            raise IOError("If an input file has not been defined, the endpoints must be specified as arguments.")
        a, b, alpha, n = args.a, args.b, args.alpha, args.n

    check_input_params(a, b, n)

    if args.output_file:
        args.output_file.write("This is Euler's Method.\n")
        _ = eulers_method(
            function=function, a=a, b=b, alpha=alpha, n=n, file=args.output_file, table_output=True
        )
        args.output_file.close()
    else:
        print("This is Euler's Method.")
        _ = eulers_method(
            function=function, a=a, b=b, alpha=alpha, n=n, file=None, table_output=args.table_output
        )


if __name__ == "__main__":
    main()
