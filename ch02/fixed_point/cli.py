#!/usr/bin/env python3
import argparse
from typing import TextIO

from fixed_point import fixed_point


def predefined_function(x: float) -> float:
    return x**3 + 4.0 * x**2 - 10.0


def parse_file_input(input_file: TextIO) -> dict:
    """Parse the initial approximation, tolerance, and maximum number of inputs supplied in a CSV file."""
    vals = input_file.read().split(",")
    p_0: float = float(vals[0])
    tol: float = float(vals[1])
    n_0: int = int(vals[2])

    return {"p_0": p_0, "tol": tol, "n_0": n_0}


def check_input_params(tol: float, n_0: int) -> None:
    """Check that the tolerance and the number of iterations are positive."""
    # check that TOL > 0
    if tol <= 0.0:
        raise IOError("Tolerance must be a positive number.")

    # check that n_0 > 0
    if n_0 <= 0:
        raise IOError("Maximum number of iterations must be a positive integer.")


def main():
    parser = argparse.ArgumentParser(description=fixed_point.__doc__)

    parser.add_argument(
        "p_0", nargs="?", default=None, type=float, help="The initial approximation."
    )
    parser.add_argument(
        "--function",
        nargs="?",
        default=None,
        type=str,
        help="A function continuous in some neighbourhood of p_0.",
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
        if args.p_0:
            raise IOError(
                "If an input file has been defined, no other input parameters must be defined."
            )
        params = parse_file_input(args.input_file)
        p_0, tol, n_0 = params["p_0"], params["tol"], params["n_0"]
    else:
        if args.p_0 is None:
            raise IOError(
                "If an input file has not been defined, the initial approximation must be specified as an argument."
            )
        p_0, tol, n_0 = args.p_0, args.tol, args.n_0

    check_input_params(tol, n_0)

    if args.output_file:
        print("")
        args.output_file.write("This is the Fixed-point Iteration Algorithm.\n")
        _ = fixed_point(
            function=function,
            p_0=p_0,
            tol=tol,
            n_0=n_0,
            file=args.output_file,
            table_output=True,
        )
        args.output_file.close()
    else:
        print("This is the Fixed-point Iteration Algorithm.")
        _ = fixed_point(
            function=function,
            p_0=p_0,
            tol=tol,
            n_0=n_0,
            file=None,
            table_output=args.table_output,
        )


if __name__ == "__main__":
    main()
