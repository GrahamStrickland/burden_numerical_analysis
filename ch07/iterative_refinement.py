# 7.4 Iterative Refinement
# To approximate the solution to the linear system Ax = b:
# Input: the number of equations and unknowns n;
#        the entries a[i,j], 1 <= i, j <= n of the matrix A;
#        the entries b[i], 1 <= i <= n of b;
#        maximum number of iterations N; tolerance TOL;
#        number of digits precision t.
# Output: the approximation xx = (xx[i],...,xx[n]) or a message
#         that the number of iterations was exceeded, and an
#         approximation COND to K∞(A).
import numpy as np


def inp(OK, n, A, b, N, TOL, t):
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

    # Fill array coefficients
    OK = False
    while not OK:
        print("Please enter the coefficients for matrix A: ")
        for i in range(n):
            print(f"Row {i+1}:")
            for j in range(n):
                A[i, j] = float(input(f"A[{i+1}, {j+1}]: "))
        print("Please enter the values of the column vector b: ")
        for k in range(n):
            b[k] = float(input(f"b[{k+1}]: "))
        OK = True

    if OK:
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

        # input tolerance TOL
        OK = False
        while not OK:
            TOL = float(input("Please input a value for the tolerance (TOL): "))

            if TOL <= 0.0:
                print("TOL must be a positive value.")
            else:
                OK = True

        # input precision t
        OK = False
        while not OK:
            t = int(
                input("Please input a value for the number of digits precision (t): ")
            )

            if t <= 0:
                print("t must be a positive value.")
            else:
                OK = True

    return OK, n, A, b, N, TOL, t


# Function to solve system using Gaussian Elimination
def solve(OK, A, x, n, t):
    if OK:
        i = 0
        n_n = n - 1
        m = n + 1

        while OK and i < n_n:
            # Find p
            p = i
            while p < n and abs(A[p, i]) == 0:
                p += 1

            if p == n:
                OK = False
            else:
                # If p != i then perform (Ep) <-> (Ei).
                if p != i:
                    temp = np.array(A[p, :])
                    A[p, :] = A[i, :]
                    A[i, :] = temp

                # For j = i + 1, ..., n do Steps 5 and 6.
                for j in range(i + 1, n):
                    # Set m(j,i) = a(j,i)/a(i,i).
                    val = A[j, i] / A[i, i]
                    x_m = np.round(val, decimals=t)

                    # Perform (Ej - m(j,i)*Ei) -> (Ej)
                    for k in range(n + 1):
                        val = A[j, k] - (x_m * A[i, k])
                        A[j, k] = np.round(val, decimals=t)
                    A[j, i] = 0.0
            i += 1
        if OK:
            # If a(n,n) = 0 terminate.
            if A[n - 1, n - 1] == 0.0:
                print("No unique solution exists.")
                OK = False
            else:
                # Start backward substitution.
                val = A[n - 1, m - 1] / A[n - 1, n - 1]
                x[n - 1] = np.round(val, decimals=t)

                # Determine xi
                for i in range(n - 2, -1, -1):
                    sum = 0.0
                    for j in range(i + 1, n):
                        sum += A[i, j] * x[j]
                    val = (A[i, n] - sum) / A[i, i]
                    x[i] = np.round(val, decimals=t)
            return OK, A, x
        else:
            print("No unique solution exists.")


def main():
    OK = False
    n = 0
    A = np.empty(0)
    b = np.empty(0)
    N = 0
    TOL = 0.0
    t = 0

    print("This is the Iterative Refinement method.")

    OK, n, A, b, N, TOL, t = inp(OK, n, A, b, N, TOL, t)
    x = np.zeros(n)
    b = np.reshape(b, (n, 1))
    A = np.append(A, b, axis=1)

    # STEP 0: Gaussian elimination
    OK, A, x = solve(OK, A, x, n, t)
    print(A)

    if OK:
        # STEP 1: Set k = 1.
        k = 1
        r = np.zeros(n)
        y = np.zeros(n)
        xx = np.zeros(n)
        b = A[:, n]

        # STEP 2: While (k <= N) do Steps 3-9.
        while k <= N and OK:
            # STEP 3: For i = 1,2,...,n calculate r.
            for i in range(n):
                sum = 0.0
                for j in range(n):
                    sum += A[i, j] * x[j]
                r[i] = b[i] - sum
            # STEP 4: Solve the linear system Ay = r by using Gaussian elimination.
            A[:, n] = r
            OK, A, y = solve(OK, A, y, n, 10)

            # STEP 5: For i = 1,...,n set xx[i] = x[i] + y[i].
            for i in range(n):
                xx[i] = x[i] + y[i]

            # STEP 6: If k = 1 then set COND = (||y||∞/||xx||∞)*10^t.
            if k == 1:
                norm1 = abs(y[0])
                norm2 = abs(xx[0])
                for i in range(n):
                    if abs(y[i]) > norm1:
                        norm1 = abs(y[i])
                    if abs(xx[i] > norm2):
                        norm2 = abs(xx[i])
                COND = (norm1 / norm2) * 10**t

            # STEP 7: If ||x - xx||∞ < TOL then the procedure was successful.
            norm3 = abs(x[0] - xx[0])
            for i in range(n):
                if abs(x[i] - xx[i]) > norm3:
                    norm3 = abs(x[i] - xx[i])
            if norm3 < TOL:
                print(f"COND = {COND}")
                print(f"The procedure was successful after {k} iterations.")
                print(f"||x - x0|| = {norm3}, < TOL = {TOL}")
                OK = False

            # STEP 8: Set k = k + 1.
            k = k + 1

            # STEP 9: For i = 1,...,n set x[i] = xx[i].
            for i in range(n):
                x[i] = xx[i]

        # STEP 10: The procedure was unsuccessful.
        if OK:
            print("The procedure was unsuccessful.")
            print(f"COND = {COND}")
            OK = False


if __name__ == "__main__":
    main()
