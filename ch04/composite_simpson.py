# 4.1 Composite Simpson's Rule
# To approximate the integral I = integral(f(x)dx) from a to b.
# Input: endpoints a, b; even positive integer n.
# Output: approximation XI to I.
import math


def inp_vals(OK, a, b, n):
    OK = False
    ans = input("Have you defined the function f before starting this program? (Y/N): ")
    if ans == "Y" or ans == "y":
        OK = True

        OK = False
        while not OK:
            # Enter amount for lower and upper bounds (a and b).
            a = float(input("Please enter a value for the lower bound (a): "))
            b = float(input("Please enter a value for the upper bound (b): "))

            # Check that b != a.
            if b == a:
                print("a and b cannot have the same value.")
            else:
                OK = True

            # if b < a, reverse order of a and b
            if b < a:
                x = a
                a = b
                b = x

        OK = False
        while not OK:
            # Input value for number of subintervals.
            n = int(input("Please input a value for the number of subintervals (n): "))

            # Check that n is an even, positive integer.
            if n <= 0 or n % 2 != 0:
                print("Number of subintervals must be an even, positive integer.")
            else:
                OK = True

        # Return values for function.
        return OK, a, b, n
    else:  # If answer is not yes, terminate program.
        print("Terminating program so that functions can be defined.")
        return


def f(x):
    return ((x - 1) ** (-1 / 5)) * (
        math.log(x)
        - (x - 1)
        + ((x - 1) ** 2) / 2
        - ((x - 1) ** 3) / 3
        + ((x - 1) ** 4) / 4
    )


def main():
    OK = False
    a = b = 0.0
    n = 0

    # Print introduction and input values.
    print("This is the Composite Simpson's rule algorithm.")
    OK, a, b, n = inp_vals(OK, a, b, n)

    if OK:
        # STEP 1: Set h.
        h = (b - a) / n

        # STEP 2: Set XI0, XI1, and XI2.
        XI0 = f(a) + f(b)
        XI1 = 0
        XI2 = 0

        # STEP 3: For i = 1,..., n-1 do Steps 4 and 5.
        for i in range(1, n):
            # STEP 4: Set X.
            X = a + i * h

            # STEP 5: If i is even then set XI2, else set XI1.
            if i % 2 == 0:
                XI2 = XI2 + f(X)
            else:
                XI1 = XI1 + f(X)

        # STEP 6: Set XI.
        XI = (h / 3) * (XI0 + 2 * XI2 + 4 * XI1)

        # STEP 7: Output result..
        print("Approximate solution XI = {:.10f}".format(XI))


if __name__ == "__main__":
    main()
