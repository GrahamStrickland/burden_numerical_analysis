#!/usr/bin/env python3
import argparse
from typing import TextIO

from pade_rational_approximation import pade_rational_approximation


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the values for m, n, and Maclaurin polynomial coefficients.""" 
    vals = input_file.read().split(',')
    m = int(vals[0])
    n = int(vals[1])
    maclaurin_coeffs = []
    for i in range(2, len(vals)):
        try:
            maclaurin_coeffs.append(float(vals[i]))
        except ValueError as _:
            break

    return {'m': m, 'n': n, 'maclaurin_coeffs': maclaurin_coeffs}


def check_input_params(
        m: int, n: int, maclaurin_coeffs: list[float]
                       ) -> list[int, int, list[float]]:
    """Check that m and n are nonnegative and that the Maclaurin coefficients
    are of order N = m + n."""
    if m < 0 or n < 0:
        raise IOError("m and n must be nonnegative integers.")

    if len(maclaurin_coeffs) != m+n+1:
        raise IOError(f"Please specify {m+n+1} Maclaurin coefficients.")

    return [m, n, maclaurin_coeffs]


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
        "--maclaurin_coeffs",
        nargs='+',
        default=None,
        type=float,
        help="The Maclaurin coefficients for the polynomial of degree m+n."
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

    if args.input_file is not None:
        if args.m or args.n or args.maclaurin_coeffs:
            raise IOError(
"""If an input file has been defined, no other input parameters must be defined."""
                )
        params = parse_file_input(args.input_file)
        m, n = params["m"], params["n"], 
        maclaurin_coeffs = params["maclaurin_coeffs"]
    else:
        if args.m is None or args.n is None:
            raise IOError(
"""If an input file has not been defined, m and n must be specified as arguments,
along with the Maclaurin coefficients a0, a1, ..., a_(m+n)"""
                )
        m, n = args.m, args.n
        maclaurin_coeffs = args.maclaurin_coeffs

    check_input_params(m, n, maclaurin_coeffs)

    if args.output_file is not None:
        args.output_file.write(
            "This is the Pade Rational Approximation.\n"
                )
        _ = pade_rational_approximation(
            m=m, n=n, file=args.output_file, maclaurin_coeffs=maclaurin_coeffs 
        )
        args.output_file.close()
    else:
        print(
            "This is the Pade Rational Approximation."
                )
        _ = pade_rational_approximation(
            m=m, n=n, file=None, maclaurin_coeffs=maclaurin_coeffs 
        )


if __name__ == "__main__":
    main()
