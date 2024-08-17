# 4.2 Romberg Integration
# To approximate the integral I = integral(f(x)dx) from a to b.
# Input: endpoints a, b; positive integer n.
# Output: an array R. (Compute R by rows; only the last two rows are saved in storage).
import math


def inp_vals(OK, a, b, n, TOL, MAX):
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
            # Input value for number of rows or tolerance.
            print("Please input a value for the number of rows (n)")
            n = int(input("Enter -1 if tolerance is to be input instead: "))

            # Check for number of rows or tolerance.
            if n <= 0:
                n = 2
                TOL = float(input("Enter a value for the tolerance: "))
                if TOL <= 0.0:
                    print("Tolerance must be greater than 0.0.")
                else:
                    MAX = int(input("Please enter a maximum number of rows: "))
                    if MAX < 0:
                        print("Upper bound must be positive.")
                    else:
                        OK = True
            else:
                TOL = 0.0
                MAX = 0
                OK = True

        # Return values for function.
        return OK, a, b, n, TOL, MAX
    else:  # If answer is not yes, terminate program.
        print("Terminating program so that functions can be defined.")
        return


def f(x):
    return math.cos(x) ** 2


def main():
    OK = False
    a = b = TOL = 0.0
    n = MAX = 0

    # Print introduction and input values.
    print("This is the Romberg Integration algorithm.")
    OK, a, b, n, TOL, MAX = inp_vals(OK, a, b, n, TOL, MAX)
    R = [[0.0 for _ in range(n)], [0.0 for _ in range(n)]]

    if OK:
        # STEP 1: Set h.
        h = b - a
        R[0][0] = (h / 2) * (f(a) + f(b))

        # STEP 2: Output R[1,1].
        print("\nR[1]\t{:.8f}".format(R[0][0]))

        # STEP 3: For i = 2,..., n do Steps 4-8.
        i = 1
        while i < n:
            # STEP 4: Set R[2,1] (Approximation from Trapezoidal method).
            sum = 0.0
            exponent = int(2 ** (i - 1))
            for k in range(1, exponent + 1):
                sum += f(a + (k - 0.5) * h)
            R[1][0] = 0.5 * (R[0][0] + h * sum)

            # STEP 5: For j = 2,..., i set R[2,j] (Extrapolation).
            for j in range(1, i + 1):
                R[1][j] = R[1][j - 1] + (R[1][j - 1] - R[0][j - 1]) / (4**j - 1)

            # STEP 6: Output R[2,j] for j = 1, 2,..., i.
            str = f"R[{i+1}]\t"
            for j in range(i + 1):
                str = str + "{:.8f}\t".format(R[1][j])
            print(str)

            # STEP 7: Set h.
            h /= 2

            # Check tolerance and update R if necessary.
            if TOL > 0.0:
                if abs(R[1][i] - R[0][i - 1]) > TOL and i + 1 < MAX:
                    n = n + 1
                    R[0].append(0.0)
                    R[1].append(0.0)

            # STEP 8: For j = 1, 2,..., i update row 1 of R.
            for j in range(i + 1):
                R[0][j] = R[1][j]

            # Increment iterator.
            i = i + 1

    # STEP 9: Stop.


if __name__ == "__main__":
    main()
