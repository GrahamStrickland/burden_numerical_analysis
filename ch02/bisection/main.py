#!/usr/bin/env python3
import argparse
import bisection
import math


def f(x: float) -> float:
    return 2.0 - (x * math.exp(x))


def parse_file_input(*args) -> None:
    pass


def parse_console_input(*args) -> None:
    # check if function has been assigned
    ans = input("Have you defined the function f before starting this program? (Y/N): ")
    if ans == 'Y' or ans == 'y':
        # enter amount for lower and upper bounds (a and b)
        a: float = input("Please enter a value for the lower bound (a): ")
        b: float = input("Please enter a value for the upper bound (b): ")

        # check that b != a
        if b == a:
            print("a and b cannot have the same value.")
            return []

        # if b < a then reverse order of a and b
        if b < a:
            x: float = a
            a = b
            b = x

        # define f(a) and f(b)
        f_a: float = f(a)
        f_b: float = f(b)

        # check that f(a) and f(b) have different signs
        if f_a * f_b > 0.0:
            print("f(a) and f(b) cannot have the same sign.")
            return []

        # input value for tolerance
        tol: float = input("Please input a value for the tolerance: ")

        # check that TOL > 0
        if tol <= 0.0:
            print("Tolerance must be a positive number.")
            return []

        # input value for maximum number of iterations
        n_0: int = input("Please input a value for the maximum number of iterations (N0): ")

        # check that N0 > 0
        if n_0 <= 0:
            print("Maximum number of iterations must be a positive integer.")
            return []

        # return values for function
        return [a, b, tol, n_0]

    else:   # if answer is not yes, terminate program
        print("Terminating program so that functions can be defined.")
        return []


def get_input_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        name="-f",
        help="flag for file input",
        action="store_true"
    )
    group.add_argument(
        name="-c",
        help="flag for console input",
        action="store_true"
    )
    parser.add_argument(
        name="input_file",
        type=argparse.FileType('r'),
        help="name of input file",
        required=True
    )
    parser.add_argument(
        name="output_file",
        type=argparse.FileType('w'),
        help="name of output file",
        required=False
    )
    parser.add_argument(
        name="a",
        type=float,
        help="left endpoint of the interval",
        required=True
    )
    parser.add_argument(
        name="b",
        type=float,
        help="right endpoint of the interval",
        required=True
    )
    parser.add_argument(
        name="tol",
        type=float,
        help="tolerance for function",
        required=True
    )
    parser.add_argument(
        name="n_0",
        type=int,
        help="maximum number of iterations",
        required=True
    )
    parser.add_argument(
        name="output_file",
        type=argparse.FileType('w'),
        help="name of output file",
        required=False
    )

    args = parser.parse_args()

    if args.file_input:
        parse_file_input(args.file_input)
    else:
        parse_console_input(args.console_input)

    return args


def main() -> None:
    # print introduction
    print("This is the Bisection Algorithm")

    if output_file:
        open(file=output_file, mode='w')
        output_file.write(output_string)
        p: float = bisection.Bisection(a, b, tol, n_0, output_file)
    else:
        print(output_string)
        p: float = bisection.Bisection(a, b, tol, n_0)

    print("p = {:.10f}".format(p))


if __name__ == "__main__":
    main()
