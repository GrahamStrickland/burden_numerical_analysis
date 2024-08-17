# 7.1 Jacobi Iterative Method
# To solve Ax = b given an initial approximation x0:
# Input: the number of equations and unknowns n;
#        the entries a[i,j], 1 <= i, j <= n of the matrix A;
#        the entries b[i], 1 <= i <= n of b; the entries XO[i],
#        of XO = x0; tolerance TOL; maximum number of iterations N.
# Output: the approximate solution x[1],...,x[n] or a message that the
#         number of iterations was exceeded.
import numpy as np


def inp(OK, n, A, b, XO, TOL, N):
    OK = False

    # Input n
    while not OK:
        n = int(input("Please input the number of unkowns and equations (n): "))
        if n <= 0:
            print("Must be a positive integer value.")
        else:
            OK = True

    # Declare A as uninitialized array
    A = np.empty([n, n])
    b = np.empty(n)
    XO = np.empty(n)

    # Fill array coefficients
    OK = False
    while not OK:
        print("Please enter the coefficients for matrix A: ")
        for i in range(n):
            print(f"Row {i+1}:")
            for j in range(n):
                A[i, j] = np.double(input(f"A[{i+1}, {j+1}]: "))
        print("Please enter the values of the column vector b: ")
        for k in range(n):
            b[k] = np.double(input(f"b[{k+1}]: "))
        print("Please enter the initial approximations for x0: ")
        for l in range(n):
            XO[l] = np.double(input(f"x0[{l+1}]: "))
        OK = True

    if OK:
        # input tolerance TOL
        OK = False
        while not OK:
            TOL = float(input("Please input a value for the tolerance (TOL): "))

            if TOL <= 0.0:
                print("TOL must be a positive value.")
            else:
                OK = True

        # input maximum number of iterations
        OK = False
        while not OK:
            N = int(
                input("Please enter a value for the maximum number of iterations (N): ")
            )

            if N <= 0:
                print("N0 must be a positive value.")
            else:
                OK = True

    return OK, n, A, b, XO, TOL, N


def main():
    OK = False
    n = 0
    A = np.empty(0)
    XO = np.empty(0)
    b = np.empty(0)
    TOL = 0.0
    N = 0

    OK, n, A, b, XO, TOL, N = inp(OK, n, A, b, XO, TOL, N)
    x = np.zeros(n)

    print("This is the Jacobi Iterative Method.")

    if OK:
        # STEP 1: Set k = 1.
        k = 1

        # STEP 2: While (k <= N) do Steps 3-6.
        while k <= N and OK:
            # STEP 3: For i = 1,...,n set x[i]
            for i in range(n):
                sum = 0.0
                for j in range(n):
                    if j != i:
                        sum += A[i, j] * XO[j]
                x[i] = (-sum + b[i]) / A[i, i]

            print(f"Iteration {k}:")
            for i in range(n):
                print(f"x[{i+1}] = {x[i]}")

            # STEP 4: If ||x - XO|| < TOL then procedure was successful.
            norm = abs(x[0] - XO[0])
            for i in range(n):
                if abs(x[i] - XO[i]) > norm:
                    norm = abs(x[i] - XO[i])
            if norm < TOL:
                print(f"The procedure was successful after {k} iterations.")
                print(f"||x - x0|| = {norm}, < TOL = {TOL}")
                OK = False

            if OK:
                # STEP 5: Set k = k + 1.
                k = k + 1

                # STEP 6: For i = 1,...,n set XO[i] = x[i].
                for i in range(n):
                    XO[i] = x[i]

    # STEP 7: The procedure was not successful.
    if OK:
        print("The procedure was not successful.")
        OK = False


if __name__ == "__main__":
    main()
