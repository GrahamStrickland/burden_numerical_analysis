# 3.6 Bézier Curve
# To construct the cubic Bézier curves C[0],..., C[n-1] in parametric form,
# where C[i] is represented by (x(t), y[i](t)) = (a[0]^i + a[1]^i*t + a[2]^i*t**2
#                                                + a[3]^i*t**3, b[0]^i + b[1]^i*t
#                                                + b[2]^i*t**2 + b[3]^i*t**3),
#                                                for 0 <= t <= 1,
# as determine by the left endpoint (x[i], y[i]),
# left guidepoint (x[i]^(+), y[i]^(+)),
# right endpoint (x[i+1], y[i+1]),
# and right guidepoint (x[i+1]^(-), y[i+1]^(-)) for each i = 0, 1,..., n-1:
# Input: n; (x[0], y[0]),..., (x[n], y[n]);
#        (x^(+)[0], y^(+)[0]),..., (x^(+)[n-1], y^(+)[n-1]);
#        (x^(-)[0], y^(-)[0]),..., (x^(-)[n], y^(-)[n]).
# Output: coefficients {a[0]^i, a[1]^i, a[2]^i, a[3]^i,
#         b[0]^i, b[1]^i, b[2]^i, b[3]^i, for 0 <= i <= n-1}.


# Function for value input.
def inp(OK, n, x, y):
    # Input n.
    OK = False
    while not OK:
        n = int(input("Please enter the number of approximations (n): "))
        if n > 0:
            OK = True
        else:
            print("Please enter a positive value for n.")

    # Assign (x[0], y[0]),..., (x[n], y[n]).
    OK = False
    while not OK:
        print("Please enter the values for the endpoints (x0, y0),..., (xn, yn): ")
        for i in range(n + 1):
            x[0].append(float(input(f"x{i}: ")))
            y[0].append(float(input(f"y{i}: ")))
        print(
            "Please enter the values for the guidepoints (x0+, y0+),..., (xn+, yn+): "
        )
        for i in range(n):
            x[1].append(float(input(f"x{i}+: ")))
            y[1].append(float(input(f"y{i}+: ")))
        print(
            "Please enter the values for the guidepoints (x0-, y0-),..., (xn-, yn-): "
        )
        for i in range(n):
            x[2].append(float(input(f"x{i + 1}-: ")))
            y[2].append(float(input(f"y{i + 1}-: ")))

        OK = True

    return OK, n, x, y


def main():
    # Assign initial variables.
    OK = False
    n = 0
    x = [[], [], []]
    y = [[], [], []]

    # Print introduction and input values.
    print("This is the Bézier curve algorithm.")
    OK, n, x, y = inp(OK, n, x, y)
    a = [[], [], [], []]
    b = [[], [], [], []]

    if OK:
        # STEP 1: For each i = 0, 1,..., n-1 do Steps 2 and 3.
        for i in range(n):
            # STEP 2: Set values for a and b.
            a[0].append(x[0][i])
            b[0].append(y[0][i])
            a[1].append(3 * (x[1][i] - x[0][i]))
            b[1].append(3 * (y[1][i] - y[0][i]))
            a[2].append(3 * (x[0][i] + x[2][i] - 2 * x[1][i]))
            b[2].append(3 * (y[0][i] + y[2][i] - 2 * y[1][i]))
            a[3].append(x[0][i + 1] - x[0][i] + 3 * x[1][i] - 3 * x[2][i])
            b[3].append(y[0][i + 1] - y[0][i] + 3 * y[1][i] - 3 * y[2][i])

            # STEP 3: OUTPUT.
            if i == 0:
                print("-" * 68)
                print("i\ta0\ta1\ta2\ta3\tb0\tb1\tb2\tb3")
                print("-" * 68)
            print(
                f"{i}\t{a[0][i]}\t{a[1][i]}\t{a[2][i]}\t{a[3][i]}\t{b[0][i]}\t{b[1][i]}\t{b[2][i]}\t{b[3][i]}\t"
            )

        # STEP 4: STOP.


if __name__ == "__main__":
    main()
