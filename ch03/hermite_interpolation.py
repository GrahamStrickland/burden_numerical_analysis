# f3.3 Hermite Interpolation
# To obtain the coefficients of the Hermite interpolating polynomial H(x)
# at the (n+1) distinct numbers x0, x1,..., xn for the function f:
# Input: numbers x0, x1,..., xn; values f(x0),..., f(xn)
#        and f'(x0),..., f'(xn).
# Output: the numbers Q[0,0], Q[1,1],..., Q[2n+1, 2n+1] where
#         H(x) = Q[0,0] + Q[1,1](x-x0) + Q[2,2](x-x0)^2 + Q[3,3](x-x0)^2(x-x1)
#                + Q[4,4](x-x0)^2(x-x1)^2 + ...
#                + Q[2n+1][2n+1](x-x0)^2(x-x1)^2...(x-x[n-1])^2(x-xn).

# Function for value input.
def inp(OK, n, x, f, fP):
    # Input n.
    OK = False
    while not OK:
        n = int(input("Please enter the number of points to be input (n): "))
        if n > 0:
            OK = True
        else:
            print("Please enter a positive value for n.")

    # Assign xi, f(xi), f'(xi) for 1,...,n.
    OK = False
    while not OK:
        print("Please enter the values for the points x0, x1,..., xn: ")
        for i in range(n):
            x.append(float(input(f"x{i}: ")))
        print("Please enter the function values f(x0),...,f(xn): ")
        for j in range(n):
            f.append(float(input(f"f(x{j}): ")))
        print("Please enter the 1st derivative values f'(x0),...,f'(xn): ")
        for k in range(n):
            fP.append(float(input(f"f'(x{k}): ")))

        OK = True

    return OK, n, x, f, fP


def main():
    # Assign initial variables.
    OK = False
    n = 0
    x = []
    f = []
    fP = []

    # Print introduction and input values.
    print("This is the Hermite Interpolation method.")
    OK, n, x, f, fP = inp(OK, n, x, f, fP)

    # Declare arrays z and Q with values of None.
    z = [None for i in range(2 * n)]
    Q = [[None for i in range(2 * n)] for j in range(2 * n)]

    if OK:
        # STEP 1: For i = 0, 1,..., n do Steps 2 and 3.
        for i in range(n):
            # STEP 2: Set z[2i] = xi;
            #             z[2i+1] = xi;
            #             Q[2i,0] = f(xi);
            #             Q[2i+1,0] = f(xi);
            #             Q[2i+1,1] = f'(xi);
            z[2 * i] = x[i]
            z[2 * i + 1] = x[i]
            Q[2 * i][0] = f[i]
            Q[2 * i + 1][1] = fP[i]
            Q[2 * i + 1][0] = Q[2 * i][0]

            # STEP 3: If i != 0 then set Q[2i,1] = (Q[2i,0] - Q[2i-1,0]) / (z[2i] - z[2i-1]).
            if i != 0:
                Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (
                    z[2 * i] - z[2 * i - 1]
                )

        # STEP 4: For i = 2, 3,...., 2n+1
        #           for j = 2, 3,..., i set Q[i,j] = (Q[i,j-1] - Q[i-1,j-1]) / (z[i] - z[i-j]).
        for i in range(2, 2 * n):
            for j in range(2, i + 1):
                Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])

        # STEP 5: OUTPUT(Q[0,0], Q[1,1],..., Q[2n+1,2n+1]);
        #         STOP.
        print("The Coefficients of the Hermite Interpolation Polynomial")
        print("in order of increasing exponent follow:")
        for k in range(2 * n):
            print("Q[{},{}] = {}".format(k, k, Q[k][k]))
        print("Do you wish to evaluate this polynomial?")
        ans = input("Enter Y or N: ")
        if ans == "Y" or ans == "y":
            p = float(input("Enter a point at which to evaluate: "))
            S = Q[2 * n - 1][2 * n - 1] * (p - z[2 * n - 1])
            for i in range(2, 2 * n):
                S = (S + Q[2 * n - i][2 * n - i]) * (p - z[2 * n - i - 1])
            S = S + Q[0][0]
            print("Interpolated-value: {}".format(S))


if __name__ == "__main__":
    main()

