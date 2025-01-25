# 3.2 Newton's Divided-Difference Formula
# To obtain the divided-difference coefficients of the interpolatory
# polynomial P on the (n+1) distinct numbers x0, x1,..., xn for the function f:
# Input: numbers x0, x1,..., xn; values f(x0), f(x1),..., f(xn)
#        as F[0,0], F[1,0],..., F[n,0].
# Output: the numbers F[0,0], F[1,1],..., F[n,n] where
#         Pn(x) = F[0,0] + sum(F[i,i] * product(x - xj) for j = 0 through i - 1)
#         for i = 1 through n. (F[i,i] is f[x0, x1,..., xi].)

# function for value input
def inp(OK, n, xvals, F):
    # Input n
    OK = False
    while not OK:
        n = int(input("Please enter the number of points to be input (n): "))
        if n > 0:
            OK = True
        else:
            print("Please enter a positive value for n.")

    # Populate F as empty nested list
    for i in range(n):
        F.append([None for j in range(n)])

    # Assign x, xi for 1,...,n and F[i,0] for 1,....,n
    OK = False
    while not OK:
        print("Please enter the values for the points x0, x1,..., xn: ")
        for i in range(n):
            xvals.append(float(input(f"x{i}: ")))
        print("Please enter the function values f(xi) at the points x0, x1,..., xn: ")
        for j in range(n):
            F[j][0] = float(input(f"f(x{j}): "))
        OK = True

    return OK, n, xvals, F


def main():
    # Assign initial variables
    OK = False
    n = 0
    xvals = []
    F = []

    # Print introduction and input values
    print("This is Newton's Divided-Difference Formula.")
    OK, n, xvals, F = inp(OK, n, xvals, F)

    if OK:
        # STEP 1: Set F[i,j] for each value
        for i in range(1, n):
            for j in range(1, i + 1):
                F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (xvals[i] - xvals[i - j])

        # STEP 2: Output values in table format
        for j in range(n):
            print("F[{}][{}] = {}".format(j, j, F[j][j]))


if __name__ == "__main__":
    main()
