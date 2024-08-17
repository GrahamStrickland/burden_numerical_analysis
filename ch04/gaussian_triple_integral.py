# 4.6 Gaussian Triple Integral
# To approximate I = triple integral ( ( f(x,y,z) dz dy dx ) ) with limits
# of integration from a to b for x, from c(x) to d(x) for y, and from
# alpha(x,y) to beta(x,y) for z.
# Input: endpoints a, b; positive integers m, n, & p.
#        (The roots r[i,j] and coefficients c[i,j] need to be available
#         for i = max{m,n} and for 1 <= j <= i.)
# Output: approximation J to I.
import math


def inp_vals(OK, a, b, m, n, p):
    OK = False
    ans = input(
        "Have you defined the functions f(x), c(x), d(x), alpha(x,y), and beta(x, y)\nbefore starting this program? (Y/N): "
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

        # Input m, n, & p.
        print("\nInput three integers m, n, & p.")
        print("This implementation of Gaussian quadrature requires")
        print("that they are greater than 1 and less than or equal to 5.")
        print("They will be used in first, second, and third dimensions, respectively.")

        OK = False
        while not OK:
            # Input value for m.
            m = int(input("Please input a value for m: "))

            # Check that n is in correct range.
            if m < 1 or m > 5:
                print("m must be greater than 1 and less than or equal to 5.")
            else:
                OK = True

        OK = False
        while not OK:
            # Input value for n.
            n = int(input("Please input a value for n: "))

            # Check that n is in correct range.
            if n < 1 or n > 5:
                print("n must be greater than 1 and less than or equal to 5.")
            else:
                OK = True

        OK = False
        while not OK:
            # Input value for p.
            p = int(input("Please input a value for p: "))

            # Check that p is in correct range.
            if p < 1 or p > 5:
                print("p must be greater than 1 and less than or equal to 5.")
            else:
                OK = True

        # Return values for function.
        return OK, a, b, m, n, p
    else:  # If answer is not yes, terminate program.
        print("Terminating program so that functions can be defined.")
        return


def f(x, y, z):
    return z * math.sqrt(x**2 + y**2)


def c(x):
    return -math.sqrt(4 - x**2)


def d(x):
    return math.sqrt(4 - x**2)


def alpha(x, y):
    return math.sqrt(x**2 + y**2)


def beta(x, y):
    return 2


def main():
    OK = False
    a = b = 0.0
    m = n = p = 0
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
    print("This is the Gaussian triple integral algorithm.")
    OK, a, b, m, n, p = inp_vals(OK, a, b, m, n, p)

    if OK:
        # STEP 1: Set intervals.
        h1 = (b - a) / 2
        h2 = (b + a) / 2
        J = 0

        # STEP 2: Loop Steps 3-8.
        for i in range(1, m + 1):
            # STEP 3: Set values for outer integral.
            JX = 0
            x = h1 * r[m - 2][i - 1] + h2
            d1 = d(x)
            c1 = c(x)
            k1 = (d1 - c1) / 2
            k2 = (d1 + c1) / 2

            # STEP 4: Loop Steps 5-7.
            for j in range(1, n + 1):
                # STEP 5: Set values for first inner integral.
                JY = 0
                y = k1 * r[n - 2][j - 1] + k2
                beta1 = beta(x, y)
                alpha1 = alpha(x, y)
                l1 = (beta1 - alpha1) / 2
                l2 = (beta1 + alpha1) / 2

                # STEP 6: Loop values for second inner integral.
                for k in range(1, p + 1):
                    z = l1 * r[p - 2][k - 1] + l2
                    Q = f(x, y, z)
                    JY = JY + co[p - 2][k - 1] * Q

                # STEP 7: Set approximation and end Step 4.
                JX = JX + co[n - 2][j - 1] * l1 * JY

            # STEP 8: Set approximation and end Step 2.
            J = J + co[m - 2][i - 1] * k1 * JX

        # STEP 9: Set approximation J.
        J = h1 * J

        # STEP 10: Output J.
        print(f"\nThe integral of f from {a} to {b} is")
        print("{:.10f} obtained with n = {}, m = {}, and p = {}.".format(J, n, m, p))


if __name__ == "__main__":
    main()
