# 3.1 Neville's Iterated Interpolation
# To evaluate the interpolating polynomial P on the n+1 distinct numbers
# x0,..., xn at the number x for the function f:
# Input: numbers x, x0, x1,..., xn; values f(x0), f(x1),..., f(xn)
#        as the first column Q[0,0], Q[1,0],..., Q[n,0] of Q.
# Output: the table Q with P(x) = Q[n,n].

# function for value input
def inp(OK, n, x, xvals, Q):
    # Input n
    OK = False
    while not OK:
        n = int(input("Please enter the number of points to be input (n): "))
        if n > 0:
            OK = True
        else:
            print("Please enter a positive value for n.")

    # Populate Q as empty nested list
    for i in range(n):
        Q.append([None for j in range(n)])

    # Assign x, xi for 1,...,n and Q[i,0] for 1,....,n
    OK = False
    while not OK:
        x = float(
            input("Please enter the value to be evaluated using Neville's method (x): ")
        )
        print("Please enter the values for the points x0, x1,..., xn: ")
        for i in range(n):
            xvals.append(float(input(f"x{i}: ")))
        print("Please enter the function values f(xi) at the points x0, x1,..., xn: ")
        for j in range(n):
            Q[j][0] = float(input(f"f(x{j}): "))
        OK = True

    return OK, n, x, xvals, Q


# function for table output
def output(n, x, xvals, Q, prec1, prec2):
    print("-" * (n + 1) * 12)
    print("i\t", "xi\t", "x-xi\t", "".join(["Qi{i}\t" for i in range(n)]))
    print("-" * (n + 1) * 12)
    for j in range(n):
        print(
            f"{j}\t",
            f"{xvals[j]}\t",
            "{:.{}f}\t".format(x - xvals[j], prec1),
            "".join(["{:.{}f}\t".format(Q[j][i], prec2) for i in range(j + 1)]),
        )
    print("-" * (n + 1) * 12)


def main():
    # Assign initial variables
    OK = False
    n = 0
    x = 0
    xvals = []
    Q = []

    # Print introduction and input values
    print("This is Neville's Iterated Interpolation method.")
    OK, n, x, xvals, Q = inp(OK, n, x, xvals, Q)

    if OK:
        # STEP 1: Set Q[i,j] for each value
        for i in range(1, n):
            for j in range(1, i + 1):
                Q[i][j] = (
                    ((x - xvals[i - j]) * Q[i][j - 1])
                    - ((x - xvals[i]) * Q[i - 1][j - 1])
                ) / (xvals[i] - xvals[i - j])

        # STEP 2: Output values in table format
        output(n, x, xvals, Q, 1, 4)


if __name__ == "__main__":
    main()

