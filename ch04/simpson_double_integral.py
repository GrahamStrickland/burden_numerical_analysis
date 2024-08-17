# 4.4 Simpson's Double Integral
# To approximate the double integral ( ( f(x,y) dy dx ) ) with limits
# of integration from a to b for x and from c(x) to d(x) for y.
# Input: endpoints a, b; even positive integers m, n.
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

        OK = False
        while not OK:
            print("Input two even, positive integers n, m.")
            print("There will be 2n subintervals for outer")
            print("integral and 2m subintervals for inner integral.")

            # Input value for n.
            n = int(input("Please input a value for n: "))

            # Check that n is a positive integer.
            if n % 2 != 0 or n <= 0:
                print("n must be an even, positive integer.")
            else:
                OK = True

        OK = False
        while not OK:
            # Input value for m.
            m = int(input("Please input a value for m: "))

            # Check that m is a positive integer.
            if m % 2 != 0 or m <= 0:
                print("m must be an even, positive integer.")
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

    # Print introduction and input values.
    print("This is the Simpson's double integral algorithm.")
    OK, a, b, m, n = inp_vals(OK, a, b, m, n)
    nn = n * 2
    mm = m * 2 - 1

    if OK:
        # STEP 1: Set interval and terms.
        h = (b - a) / nn
        J1 = 0  # (End terms.)
        J2 = 0  # (Even terms.)
        J3 = 0  # (Odd terms.)

        # STEP 2: Loop Steps 3-8.
        for i in range(nn + 1):
            # STEP 3: Composite Simpson's method for x.
            x = a + i * h
            HX = (d(x) - c(x)) / (2 * m)
            K1 = f(x, c(x)) + f(x, d(x))  # (End terms.)
            K2 = 0  # (Even terms.)
            K3 = 0  # (Odd terms.)

            # STEP 4: Loop Steps 5 and 6.
            for j in range(1, mm + 1):
                # STEP 5: Set values for inner integral.
                y = c(x) + (j * HX)
                Q = f(x, y)

                # STEP 6: Set K2 and K3.
                if j % 2 == 0:
                    K2 = K2 + Q
                else:
                    K3 = K3 + Q

            # STEP 7: Set L by the Composite Simpson's method.
            L = (HX / 3) * (K1 + 2 * K2 + 4 * K3)

            # STEP 8: Set approximation and end Step 2.
            if i == 0 or i == nn:
                J1 = J1 + L
            elif i % 2 == 0:
                J2 = J2 + L
            else:
                J3 = J3 + L

        # STEP 9: Set approximation J.
        J = (h / 3) * (J1 + 2 * J2 + 4 * J3)

        # STEP 10: Output J.
        print(f"The integral of f from {a} to {b} is")
        print("{:.10f} obtained with n = {} and m = {}.".format(J, n, m))


if __name__ == "__main__":
    main()
