# 4.5 Gaussian Double Integral
# To approximate the double integral ( ( f(x,y) dy dx ) ) with limits
# of integration from a to b for x and from c(x) to d(x) for y.
# Input: endpoints a, b; positive integers m, n.
#        (The roots r[i,j] and coefficients c[i,j] need to be available
#         for i = max{m,n} and for 1 <= j <= i.)
# Output: approximation J to I.
import math


def inp_vals(OK, a, b, m, n):
    OK = False
    ans = input(
        "Have you defined the functions f(x), c(x), and d(x)\nbefore starting this program? (Y/N): "
    )
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

        # Input m & n.
        print(
            "\nInput two positive integers n, m; there will be 2n subintervals for outer"
        )
        print("integral and 2m subintervals for inner integral.")
        print("This implementation of Gaussian quadrature requires")
        print("that they are greater than 1 and less than or equal to 5.")
        print("They will be used in first and second dimensions, respectively.")

        OK = False
        while not OK:
            # Input value for n.
            n = int(input("Please input a value for n: "))

            # Check that n is a positive integer.
            if n <= 0:
                print("n must be a positive integer.")
            else:
                OK = True

        OK = False
        while not OK:
            # Input value for m.
            m = int(input("Please input a value for m: "))

            # Check that m is a positive integer.
            if m <= 0:
                print("m must be a positive integer.")
            else:
                OK = True

        # Return values for function.
        return OK, a, b, m, n
    else:  # If answer is not yes, terminate program.
        print("Terminating program so that functions can be defined.")
        return


def f(x, y):
    return y * math.sin(x) + x * math.cos(y)


def c(x):
    return 0


def d(x):
    return 2 * math.pi


def main():
    OK = False
    a = b = 0.0
    m = n = 0
    r = [
        [
            0.5773502692,
            -0.5773502692,
        ],
        [0.7745966692, 0.0, -0.7745966692],
        [0.8611363116, 0.3399810436, -0.3399810436, -0.8611363116],
        [0.9061798459, 0.5384693101, 0.0, -0.5384693101, -0.9061798459],
    ]
    co = [
        [1.0, 1.0],
        [0.5555555556, 0.8888888889, 0.5555555556],
        [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451],
        [0.2369268850, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268850],
    ]

    # Print introduction and input values.
    print("This is the Gaussian double integral algorithm.")
    OK, a, b, m, n = inp_vals(OK, a, b, m, n)

    if OK:
        # STEP 1: Set intervals.
        h1 = (b - a) / 2
        h2 = (b + a) / 2
        J = 0

        # STEP 2: Loop Steps 3-5.
        for i in range(1, m + 1):
            # STEP 3: Set values for outer integral.
            JX = 0
            x = h1 * r[m - 2][i - 1] + h2
            d1 = d(x)
            c1 = c(x)
            k1 = (d1 - c1) / 2
            k2 = (d1 + c1) / 2

            # STEP 4: Set values for inner integral.
            for j in range(1, n + 1):
                y = k1 * r[n - 2][j - 1] + k2
                Q = f(x, y)
                JX = JX + co[n - 2][j - 1] * Q

            # STEP 5: Set approximation and end Step 2.
            J = J + co[m - 2][i - 1] * k1 * JX

        # STEP 6: Set approximation J.
        J = h1 * J

        # STEP 7: Output J.
        print(f"\nThe integral of f from {a} to {b} is")
        print("{:.10f} obtained with n = {} and m = {}.".format(J, n, m))


if __name__ == "__main__":
    main()
