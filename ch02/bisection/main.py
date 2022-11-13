#!/usr/bin/env python3
from bisection import Bisection


def f(x: float) -> float:
    return 2.0 - (x * math.exp(x))


def input_values(OK, a, b, f_a, f_b, TOL, n_0):
    # check if function has been assigned
    OK = False
    ans = input("Have you defined the function f before starting this program? (Y/N): ")
    if ans == 'Y' or ans == 'y':
        OK = True

    OK = False
    while OK == False:
        # enter amount for lower and upper bounds (a and b)
        a = float(input("Please enter a value for the lower bound (a): "))
        b = float(input("Please enter a value for the upper bound (b): "))

        # check that b != a
        if b == a:
            print("a and b cannot have the same value.")
        else:
            OK = True

        # if b < a, reverse order of a and b
        if b < a:
            x = a
            a = b
            b = x

        # define f(a) and f(b)
        f_a = f(a)
        f_b = f(b)

        # check that f(a) and f(b) have different signs
        if OK == True:
            OK = False
            if f_a * f_b > 0.0:
                print("f(a) and f(b) cannot have the same sign.")
            else:
                OK = True

    OK = False
    while OK == False:
        # input value for tolerance
        TOL = float(input("Please input a value for the tolerance: "))

        # check that TOL > 0
        if TOL <= 0.0:
            print("Tolerance must be a positive number.")
        else:
            OK = True

    OK = False
    while OK == False:
        # input value for maximum number of iterations
        n_0 = int(input("Please input a value for the maximum number of iterations (N0): "))

        # check that N0 > 0
        if n_0 <= 0:
            print("Maximum number of iterations must be a positive integer.")
        else:
            OK = True

    # return values for function
    return OK, a, b, f_a, f_b, TOL, n_0
    else: # if answer is not yes, terminate program
        print("Terminating program so that functions can be defined.")
        return




def main():
    OK = False

    # print introduction
    print("This is the Bisection Algorithm")

    # input values
    OK, a, b, f_a, f_b, TOL, n_0 = input_values(OK, a, b, f_a, f_b, TOL, n_0)

    # check if output must be table or answer only
    OK = False
    while OK == False:
        outp = int(input("Would you like to print a table (0) or the answer only (1)? "))

        if outp == 0 or outp == 1:
          OK = True

    # output table heading
    if outp == 0:
        print('-' * 80)
        print("n\t\ta\t\tb\t\tP\t\tf(P)")
        print('-' * 80)

if __name__ == "__main__":
    main()
