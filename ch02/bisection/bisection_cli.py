#!/usr/bin/env python3
import argparse
import math
from typing import Callable, TextIO

from bisection import bisect


def func(x: float) -> float:
    return x - math.exp(x)


def parse_file_input(input_file: TextIO) -> dict:
    vals = input_file.read().split(',')
    a: float = float(vals[0])
    b: float = float(vals[1])
    tol: float = float(vals[2])
    n0: int = int(vals[3])

    return {"a": a, 'b': b, 'tol': tol, 'n0': n0}


def check_input_params(f: Callable[[float], float],
                       a: float, b: float, tol: float, n0: int) -> None:
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

    # check that N0 > 0
    if n0 <= 0:
        raise IOError("Maximum number of iterations must be a positive integer.")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        name="a",
        type=float,
        required=False,
        help="The left endpoint of the interval.",
    )
    parser.add_argument(
        name="b",
        type=float,
        required=False,
        help="The right endpoint of the interval.",
    )
    parser.add_argument(
        name="--f",
        type=str,
        default=None,
        help="A function continuous on the endpoints a and b."
    )
    parser.add_argument(
        name="--tol",
        type=float,
        default=1e-6,
        help="The tolerance for the function.",
    )
    parser.add_argument(
        name="--n0",
        type=int,
        default=100,
        help="The maximum number of iterations.",
    )
    parser.add_argument(
        name="--input_file",
        type=argparse.FileType('r'),
        default=None,
        help="The name of the input file.",
    )
    parser.add_argument(
        name="--output_file",
        type=argparse.FileType('w'),
        default=None,
        help="The name of the output file.",
    )
    parser.add_argument(
        name="--table",
        type=bool,
        action="store_true",
        default=False,
        help="Flag for table output.",
    )

    args = parser.parse_args()

    if args.f:
        f = lambda: eval(args.f)
    else:
        f = func

    if args.file_input:
        params = parse_file_input(args.file_input)
        a, b, tol, n0 = params["a"], params["b"], params["tol"], params["n0"]
    else:
        if not args.a or not args.b:
            raise IOError("If an input file has not been defined, the endpoints must be input.")
        a, b, tol, n0 = args.a, args.b, args.tol, args.n0

    check_input_params(f, a, b, tol, n0)

    if args.output_file:
        args.output_file.write("This is the Bisection Algorithm.\n")
        p: float = bisect(
            function=f, a=a, b=b, tol=tol, n0=n0, file=args.output_file, table_output=True
        )
        args.output_file.write("p = {:.10f}".format(p))
        args.output_file.close()
    else:
        print("This is the Bisection Algorithm.")
        p: float = bisect(
            function=f, a=a, b=b, tol=tol, n0=n0, file=None, table_output=args.table_output
        )
        print("p = {:.10f}".format(p))


if __name__ == "__main__":
    main()
