#!/usr/bin/env python3
import bisection
import math
from typing import TextIO


def f(x: float) -> float:
    return 2.0 - (x * math.exp(x))


def input_values(file: TextIO[str]) -> list[float]:
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


def main():
    # print introduction
    print("This is the Bisection Algorithm")

    [a, b, f_a, f_b, tol, n_0] = input_values()

    output_file: str = input("Enter name of output file: ")

    # output table heading
    output_string = '-' * 80
    output_string += "n\t\ta\t\tb\t\tP\t\tf(P)"
    output_string += '-' * 80
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
