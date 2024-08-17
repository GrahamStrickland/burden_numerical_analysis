# 6.1 Gaussian Elimination with Backward Substitution
# To solve the n x n linear system
#   E1: a(1,1)x1 + a(1,2)x2 + ... + a(1,n)xn = a(1,n+1)
#   E2: a(2,1)x1 + a(2,2)x2 + ... + a(2,n)xn = a(2,n+1)
#    .      .         .                 .         .
#    :      :         :                 :         :
#   En: a(n,1)x1 + a(n,2)x2 + ... + a(n,n)xn = a(n,n+1)
# Input: number of unknowns and equations n; augmented matrix A = [a(i,j)],
#        where 1 <= i <= n and 1 <= j <= n + 1.
# Output: solution x1, x2, ..., xn or message that the linear system has
#         no unique solution.
import numpy as np


def inp(OK, n, A):
    OK = False

    # Input n
    while not OK:
        n = int(input("Please input the number of unkowns and equations (n): "))
        if n <= 0:
            print("Must be a positive integer value.")
        else:
            OK = True

    # Declare A as uninitialized array
    A = np.empty([n, n + 1])

    # Fill array coefficients
    OK = False
    while not OK:
        print("Please enter the coefficients for matrix A: ")
        for i in range(n):
            print(f"Row {i+1}:")
            for j in range(n + 1):
                A[i, j] = np.double(input(f"A[{i+1}, {j+1}]: "))
        OK = True

    return OK, n, A


def main():
    OK = False
    n = 0
    A = np.empty(0)

    print("This is Gaussian Elimination with Backward Substitution.")

    OK, n, A = inp(OK, n, A)
    x = np.empty(n)

    # Step 1: Elimination process
    if OK:
        i = 0
        n_n = n - 1
        m = n + 1
        ichg = 0
        while OK and i < n_n:
            # Step 2: Find p
            p = i
            while p < n and abs(A[p, i]) == 0:
                p += 1

            if p == n:
                OK = False
            else:
                # Step 3: If p != i then perform (Ep) <-> (Ei).
                if p != i:
                    temp = np.array(A[p, :])
                    A[p, :] = A[i, :]
                    A[i, :] = temp
                    ichg += 1

                # Step 4: For j = i + 1, ..., n do Steps 5 and 6.
                for j in range(i + 1, n):
                    # Step 5: Set m(j,i) = a(j,i)/a(i,i).
                    x_m = A[j, i] / A[i, i]

                    # Step 6: Perform (Ej - m(j,i)*Ei) -> (Ej)
                    A[j, :] = A[j, :] - (x_m * A[i, :])
                    A[j, i] = 0
            i += 1
        if OK:
            # Step 7: If a(n,n) = 0 terminate.
            if A[n - 1, n - 1] == 0:
                print("No unique solution exists.")
                OK = False
            else:
                # Step 8: Start backward substitution.
                x[n - 1] = A[n - 1, m - 1] / A[n - 1, n - 1]

                # Step 9: Determine xi
                for i in range(n - 2, -1, -1):
                    sum = 0
                    for j in range(i + 1, n):
                        sum += A[i, j] * x[j]
                    x[i] = (A[i, n] - sum) / A[i, i]

                # Step 10: Procedure completed successfully
                print("\nAfter Gaussian Elimination with Backward Substitution,")
                print(f"matrix A = \n{A}")
                print(f"Solution vector x = \n{x}")
                print(f"Number of row interchanges: {ichg}")
        else:
            print("No unique solution exists.")


if __name__ == "__main__":
    main()
