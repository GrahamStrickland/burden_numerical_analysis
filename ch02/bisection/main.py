#!/usr/bin/env python3
import argparse
import bisection
import math
from typing import TextIO


def f(x: float) -> float:
    return 2.0 - (x * math.exp(x))


def parse_file_input(input_file: TextIO) -> dict:
    vals = input_file.read().split(',')
    a: float = float(vals[0])
    b: float = float(vals[1])
    tol: float = float(vals[2])
    n0: int = int(vals[3])
    table_output: bool = vals[4] is not None

    check_input_params(a, b, tol, n0)

    return {"a": a, 'b': b, 'tol': tol, 'n0': n0, 'table_output': table_output}


def check_input_params(a: float, b: float, tol: float, n0: int) -> None:
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


def get_input_args() -> dict:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        name="input_file",
        type=argparse.FileType('r'),
        help="name of input file",
    )
    parser.add_argument(
        name="a",
        type=float,
        help="left endpoint of the interval",
    )
    parser.add_argument(
        name="b",
        type=float,
        help="right endpoint of the interval",
    )
    parser.add_argument(
        name="tol",
        type=float,
        help="tolerance for function",
    )
    parser.add_argument(
        name="n0",
        type=int,
        help="maximum number of iterations",
    )
    parser.add_argument(
        name="table_output",
        type=bool,
        help="True for table output",
    )
    parser.add_argument(
        name="output_file",
        type=argparse.FileType('w'),
        help="name of output file",
    )

    args = parser.parse_args()

    if args.file_input:
        params = parse_file_input(args.file_input)
    else:
        check_input_params(args.a, args.b, args.tol, args.n0)
        params = {'a': args.a, 'b': args.b, 'tol': args.tol, 'n0': args.n0, 'table_output': args.t}

    return params.update({'output_file': args.file_output}) if args.file_output else params


def main() -> None:
    bisect = bisection.Bisection(f)

    args: dict = get_input_args()

    a: float = args['a']
    b: float = args['b']
    tol: float = args['tol']
    n0: int = args['n0']
    table_output: bool = args['table_output']
    output_file: TextIO = args['output_file']

    if output_file:
        output_file.write("This is the Bisection Algorithm\n")
        p: float = bisect.bisect(
            a=a, b=b, tol=tol, n0=n0, table_output=True, file=output_file
        )
        output_file.write("p = {:.10f}".format(p))
        output_file.close()
    else:
        print("This is the Bisection Algorithm")
        p: float = bisect.bisect(
            a=a, b=b, tol=tol, n0=n0, table_output=table_output, file=None
        )
        print("p = {:.10f}".format(p))


if __name__ == "__main__":
    main()
