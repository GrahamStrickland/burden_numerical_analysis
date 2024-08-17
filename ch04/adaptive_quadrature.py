# 4.3 Adaptive Quadrature
# To approximate the integral I = integral(f(x)dx) from a to b.
# Input: endpoints a, b; tolerance TOL; limit N to number of levels.
# Output: approximation APP or message that N is exceeded.
import math


def inp_vals(OK, a, b, TOL, N):
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
            # Input value for TOL.
            TOL = float(input("Please input a value for the tolerance (TOL): "))

            # Check that TOL is positive.
            if TOL <= 0.0:
                print("TOL must have a positive value.")
            else:
                OK = True

        OK = False
        while not OK:
            # Input value for limit to number of levels.
            N = int(
                input(
                    "Please input a value for the limit to the number of levels (N): "
                )
            )

            # Check that n is a positive integer.
            if N <= 0:
                print("Number of subintervals must be a positive integer.")
            else:
                OK = True

        # Return values for function.
        return OK, a, b, TOL, N
    else:  # If answer is not yes, terminate program.
        print("Terminating program so that functions can be defined.")
        return


def f(x):
    return x * math.sin(x**2)


def main():
    # Declare initival values.
    OK = False
    a0 = b0 = TOL0 = 0.0
    CNT = N = 0

    # Print introduction, input values and initialize list values.
    print("This is the Adaptive quadrature algorithm.")
    OK, a0, b0, TOL0, N = inp_vals(OK, a0, b0, TOL0, N)
    a = [a0]
    TOL = [TOL0]
    h = []
    FA = []
    FB = []
    FC = []
    S = []
    L = []
    v = [None for _ in range(8)]
    for i in range(N + 1):
        a.append(None)
        TOL.append(None)
        h.append(None)
        FA.append(None)
        FB.append(None)
        FC.append(None)
        S.append(None)
        L.append(None)

    if OK:
        # STEP 1: Set list values.
        APP = 0
        i = 1
        TOL[i] = 10 * TOL[0]
        a[i] = a[0]
        h[i] = (b0 - a[0]) / 2
        FA[i] = f(a[0])
        FC[i] = f(a[0] + h[i])
        FB[i] = f(b0)
        S[i] = h[i] * (FA[i] + 4 * FC[i] + FB[i]) / 3
        L[i] = 1

        # STEP 2: While i > 0 do Steps 3-5.
        while i > 0 and OK:
            # Set list values.
            FD = f(a[i] + h[i] / 2)
            FE = f(a[i] + (3 * h[i]) / 2)

            # Approximations from Simpson's method for halves of subintervals.
            S1 = h[i] * (FA[i] + 4 * FD + FC[i]) / 6
            S2 = h[i] * (FC[i] + 4 * FE + FB[i]) / 6

            # Save data at this level.
            v[0] = a[i]
            v[1] = FA[i]
            v[2] = FC[i]
            v[3] = FB[i]
            v[4] = h[i]
            v[5] = TOL[i]
            v[6] = S[i]
            v[7] = L[i]

            # STEP 4: Delete the level.
            i = i - 1

            # STEP 5: Update APP.
            if abs(S1 + S2 - v[6]) < v[5]:
                APP = APP + (S1 + S2)
                CNT = CNT + 1
            else:
                if v[7] >= N:  # Procedure fails.
                    print("Level exceeded, procedure failed.")
                    OK = False
                else:  # Add one level.
                    # Set data for right-half subinterval.
                    i = i + 1
                    a[i] = v[0] + v[4]
                    FA[i] = v[2]
                    FC[i] = FE
                    FB[i] = v[3]
                    h[i] = v[4] / 2
                    TOL[i] = v[5] / 2
                    S[i] = S2
                    L[i] = v[7] + 1

                    # Set data for left-half subinterval.

                    i = i + 1
                    a[i] = v[0]
                    FA[i] = v[1]
                    FC[i] = FD
                    FB[i] = v[2]
                    h[i] = h[i - 1]
                    TOL[i] = TOL[i - 1]
                    S[i] = S1
                    L[i] = L[i - 1]

        # STEP 6: Procedure successful.
        if OK:
            print(
                "Integral of f over ({},{}) approximated to within {} over {} subintervals.".format(
                    a0, b0, TOL0, CNT
                )
            )
            print("Approximation = {:.10f}".format(APP))


if __name__ == "__main__":
    main()
