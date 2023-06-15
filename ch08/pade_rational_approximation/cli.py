#!/usr/bin/env python3
import argparse
import math
from typing import TextIO

from pade_rational_approximation import pade_rational_approximation


def predefined_function(x: float) -> float:
    """Predefined function in case user does not define a function."""
    return math.exp(-x)


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the values for m, n, and Maclaurin polynomial coefficients.""" 
    vals = input_file.read().split(',')
    m = int(vals[0])
    n = int(vals[1])
    coeffs = []
    for i in range(2, len(vals)):
        coeffs.append(vals[i])

    return {'m': m, 'n': n, 'maclaurin_coeffs': coeffs}


def check_input_params(
        m: int, n: int, coeffs: list[float]
                       ) -> list[int, int, list[float]]:
    """Check that m and n are nonnegative and that the Maclaurin coefficients
    are of order N = m + n."""
    if m < 0 or n < 0:
        raise IOError("m and n must be nonnegative integers.")

    if coeffs is not None and len(coeffs) != m + n:
        raise IOError(f"Please specify {m + n} Maclaurin coefficients.")

    return [m, n, coeffs]


def main():
    parser = argparse.ArgumentParser(description=pade_rational_approximation.__doc__)

    parser.add_argument(
        "m",
        nargs='?',
        default=None,
        type=int,
        help="The degree of the denominator polynomial."
    )
    parser.add_argument(
        "n",
        nargs='?',
        default=None,
        type=int,
        help="The degree of the numerator polynomial."
    )
    parser.add_argument(
        "--function",
        nargs='?',
        default=None,
        type=str,
        help="A function f(t,y) continuous on the interval [a, b]."
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

    args = parser.parse_args()

    if args.function:
        function = lambda x: eval(args.function)
    else:
        function = predefined_function

    if args.input_file:
        if args.m or args.n:
            raise IOError(
"""If an input file has been defined, no other input parameters must be defined."""
                )
        params = parse_file_input(args.input_file)
        m, n, coeffs = params["m"], params["n"], params["maclaurin_coeffs"]
    else:
        if args.m is None or args.n is None:
            raise IOError(
"""If an input file has not been defined, m and n must be specified as arguments."""
                )
        m, n = args.m, args.n
        coeffs = None

    check_input_params(m, n, coeffs)

    if args.output_file:
        args.output_file.write(
            "This is the Pade Rational Approximation.\n"
                )
        _ = pade_rational_approximation(
            function=function, m=m, n=n, file=args.output_file, 
            maclaurin_coeffs=coeffs 
        )
        args.output_file.close()
    else:
        print(
            "This is the Pade Rational Approximation."
                )
        _ = pade_rational_approximation(
            function=function, m=m, n=n, file=None, maclaurin_coeffs=coeffs 
        )


if __name__ == "__main__":
    main()
