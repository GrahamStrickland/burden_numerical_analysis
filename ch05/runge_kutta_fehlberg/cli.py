#!/usr/bin/env python3
import argparse
from collections.abc import Callable
import math
from typing import TextIO

from runge_kutta_fehlberg import runge_kutta_fehlberg


def predefined_function(t: float, y: float) -> float:
    """Predefined function in case user does not define a function."""
    return y - t**2 + 1


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the endpoints, tolerance, and maximum number of inputs 
    supplied in a CSV file."""
    vals = input_file.read().split(',')
    a = float(vals[0])
    b = float(vals[1])
    alpha = float(vals[2])
    tol = float(vals[3])
    hmax = float(vals[4])
    hmin = float(vals[5])

    return {"a": a, 'b': b, 'alpha': alpha, 'tol': tol, 'hmax': hmax, 'hmin': hmin}


def check_input_params(
        a: float, b: float, tol: float, hmax: float, hmin: float
                       ) -> list[float, float, int]:
    """Check that the endpoints are not the same, the the tolerance is positive,
    and hmax > hmin.
    """
    if b == a:
        raise IOError("a and b cannot have the same value.")

    if b < a:
        a, b = b, a

    if tol <= 0.0:
        raise IOError("Tolerance must be a positive number.")

    if hmax <= hmin:
        raise IOError("hmax must be > hmin.")

    return [a, b, tol, hmax, hmin]


def main():
    parser = argparse.ArgumentParser(description=runge_kutta_fehlberg.__doc__)

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
        default=None,
        type=float,
        help="The value y(a) = alpha."
    )
    parser.add_argument(
        "--tol",
        nargs='?',
        default=1e-6,
        type=float,
        help="The tolerance for the method."
    )
    parser.add_argument(
        "--hmax",
        nargs='?',
        default=0.25,
        type=float,
        help="The maximum step size."
    )
    parser.add_argument(
        "--hmin",
        nargs='?',
        default=0.01,
        type=float,
        help="The minimum step size."
    )
    parser.add_argument(
        "--input-file",
        nargs='?',
        default=None,
        type=argparse.FileType('r'),
        help="The name of the input file."
    )
    parser.add_argument(
        "--output-file",
        nargs='?',
        default=None,
        type=argparse.FileType('w'),
        help="The name of the output file."
    )
    parser.add_argument(
        "--solution",
        nargs='?',
        default=None,
        type=str,
        help="The solution y(t) of the given DE."
    )

    args = parser.parse_args()

    if args.function:
        function = lambda t, y: eval(args.function)
    else:
        function = predefined_function

    solution = None
    if args.solution:
        solution = lambda t: eval(args.solution)

    if args.input_file:
        if args.a or args.b or args.alpha:
            raise IOError(
                "If an input file has been defined, no other input parameters must be defined."
                )
        params = parse_file_input(args.input_file)
        a, b, alpha = params["a"], params["b"], params["alpha"]
        tol, hmax, hmin = params["tol"], params["hmax"], params["hmin"]
    else:
        if args.a is None or args.b is None or args.alpha is None:
            raise IOError(
                "If an input file has not been defined, the endpoints and initial condition must be specified as arguments."
                )
        a, b, alpha = args.a, args.b, args.alpha
        tol, hmax, hmin = args.tol, args.hmax, args.hmin

    check_input_params(a, b, tol, hmax, hmin)

    if args.output_file:
        args.output_file.write(
            "This is the Runge-Kutta-Fehlberg method of order four.\n"
                )
        _ = runge_kutta_fehlberg(
            function=function, a=a, b=b, alpha=alpha, 
            tol=tol, hmax=hmax, hmin=hmin, file=args.output_file, 
            solution=solution
        )
        args.output_file.close()
    else:
        print(
            "This is the Runge-Kutta-Fehlberg method of order four."
                )
        _ = runge_kutta_fehlberg(
            function=function, a=a, b=b, alpha=alpha, 
            tol=tol, hmax=hmax, hmin=hmin, file=None, 
            solution=solution
        )


if __name__ == "__main__":
    main()
