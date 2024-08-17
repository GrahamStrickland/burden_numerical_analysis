# 6.4 LU Factorization
# To factor the nxn matrix A = [a(i,j)] into the product of the
# lower-triangular matrix L = [l(i,j)] and the upper-triangular
# matrix U = [u(i,j)], that is, A = LU, where the main diagonal
# of either L or U consists of all 1's:
# Input: dimension n; the entries a[i,j], 1 <= i, j <= n of A;
#        the diagonal l[1,1] = ... = l[n,n] = 1 of L or
#        the diagonal u[1,1] = ... = u[n,n] = 1 of U.
# Output: the entries l[i,j], 1 <= j <= i, 1 <= i <= n of L and
#         the entries u[i,j], i <= j <= n, 1 <= i <= n of U.
import numpy as np


def inp(OK, solve, n, A, L, U, b):
    # Input dimension n
    OK = False
    while not OK:
        n = int(input("Please enter the dimension of A (n): "))
        if n <= 0:
            print("Dimension n must be a positive integer value.")
        else:
            OK = True

    # Input vector b
    OK = False
    while not OK:
        ans = input("Would you like to solve a matrix of the form Ax=b (Y/N)? ")
        if ans == "Y" or ans == "y":
            solve = True
            OK = True
        elif ans == "N" or ans == "n":
            OK = True
        else:
            print("Please enter 'Y' for yes or 'N' for no.")

    # Declare array sizes
    A = np.empty([n, n])
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    if solve:
        b = np.empty(n)

    # Fill array coefficients
    OK = False
    while not OK:
        print("Please enter the coefficients for matrix A: ")
        for i in range(n):
            print(f"Row {i+1}:")
            for j in range(n):
                A[i, j] = np.double(input(f"A[{i+1}, {j+1}]: "))
        if solve:
            print("Column vector b:")
            for k in range(n):
                b[k] = np.double(input(f"b[{k+1}]: "))
        OK = True

    # Input matrix to contain 1's along main diagonal
    OK = False
    while not OK:
        ans = input("Which matrix will contain 1's along its main diagonal? (L/U): ")
        if ans == "l" or ans == "L":
            for i in range(n):
                L[i, i] = 1.0
            OK = True
        elif ans == "u" or ans == "U":
            for i in range(n):
                U[i, i] = 1.0
            OK = True
        else:
            print("Invalid entry, please enter 'L' or 'U'.")
            OK = False

    return OK, solve, n, A, L, U, b


def main():
    OK = False
    solve = False
    n = 0
    A = np.empty(0)
    L = np.empty(0)
    U = np.empty(0)
    b = np.empty(0)

    print("This is LU Factorization.")

    OK, solve, n, A, L, U, b = inp(OK, solve, n, A, L, U, b)

    # Set flag for matrix with 1's along diagonal
    if L[0, 0] == 1.0:
        flag = True

    if OK:
        # STEP 1: Select l[1,1] and u[1,1]
        if flag:
            U[0, 0] = A[0, 0]
        else:
            L[0, 0] = A[0, 0]

        if L[0, 0] * U[0, 0] == 0.0:
            OK = False
        else:
            # STEP 2: Set u[1,j] and l[j,1]
            for j in range(1, n):
                U[0, j] = A[0, j] / L[0, 0]
                L[j, 0] = A[j, 0] / U[0, 0]

            # STEP 3: For i = 2, ..., n - 1 do Steps 4 and 5.
            for i in range(1, n - 1):
                if OK:
                    # STEP 4: Select l[i,i] and u[i,i]
                    sum = 0.0
                    for k in range(i):
                        sum += L[i, k] * U[k, i]
                    if flag:
                        U[i, i] = A[i, i] - sum
                    else:
                        L[i, i] = A[i, i] - sum

                    if L[i, i] * U[i, i] == 0.0:
                        OK = False

                    # STEP 5: Set u[i,j] and l[j,i]
                    for j in range(i + 1, n):
                        sum = 0.0
                        for k in range(i):
                            sum += L[i, k] * U[k, j]
                        U[i, j] = (A[i, j] - sum) / L[i, i]
                        sum = 0.0
                        for k in range(i):
                            sum += L[j, k] * U[k, i]
                        L[j, i] = (A[j, i] - sum) / U[i, i]

            if OK:
                # STEP 6: Select l[n,n] and u[n,n]
                sum = 0.0
                for k in range(n):
                    sum += L[n - 1, k] * U[k, n - 1]
                if flag:
                    U[n - 1, n - 1] = A[n - 1, n - 1] - sum
                else:
                    L[n - 1, n - 1] = A[n - 1, n - 1] - sum

                if L[n - 1, n - 1] * U[n - 1, n - 1] == 0.0:
                    print("A = LU but A is singular.")

                # STEP 7: Output result
                print(f"A = LU:\nL:\n{L}\nU:\n{U}")

                # STEP 8: Calculate solution vector x
                if solve:
                    y = np.empty(n)
                    x = np.empty(n)

                    # Calculate column vector y
                    y[0] = b[0] / L[0, 0]
                    for i in range(1, n):
                        sum = 0.0
                        for j in range(i):
                            sum += L[i, j] * y[j]
                        y[i] = (b[i] - sum) / L[i, i]

                    # Calculate column vector x
                    x[n - 1] = y[n - 1] / U[n - 1, n - 1]
                    for i in range(n - 2, -1, -1):
                        sum = 0.0
                        for j in range(i + 1, n):
                            sum += U[i, j] * x[j]
                        x[i] = (y[i] - sum) / U[i, i]

                    # Output vectors y and x
                    print(f"Column vector y = {y}")
                    print(f"Solution vector x = {x}")

            else:
                print("Factorization impossible.")


if __name__ == "__main__":
    main()

