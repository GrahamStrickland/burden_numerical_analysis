# Composite Midpoint Rule
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
    return x**2 * math.log(x**2 + 1)


def main():
    OK = False
    a = b = 0.0
    n = 0

    # Print introduction and input values.
    print("This is the Composite Midpoint Rule algorithm.")
    OK, a, b, n = inp_vals(OK, a, b, n)

    if OK:
        # STEP 1: Set h.
        h = (b - a) / (n + 2)

        # STEP 2: Set XI.
        XI = 0.0

        # STEP 3: For j = -1, 0,..., n+1 do Step 4.
        for j in range(-1, n + 2):
            # STEP 4: Set XJ, XI.
            XJ = a + (j + 1) * h
            if j % 2 == 0:
                XI += f(XJ)

        # STEP 5: Set XI.
        XI *= 2 * h

        # STEP 6: Output result..
        print("Approximate solution XI = {:.10f}".format(XI))


if __name__ == "__main__":
    main()
