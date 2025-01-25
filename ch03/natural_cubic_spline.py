# 3.4 Natural Cubic Spline
# To construct the cubic spline interpolant S for the function f, defined
# at the numbers x0 < x1 < ... < xn, satisfying S''(x[0]) = S''(x[n]) = 0;
# Input: n; x[0], x[1],... ,x[n]; a[0] = f(x[0]), a[1] = f(x[1]),... , a[n] = f(x[n]).
# Output: a[j], b[j], c[j], d[j] for j = 0, 1,..., n-1.
#       (Note: S(x) = S[j](x) = a[j] + bj(x - x[j]) + cj(x - x[j])**2 + dj(x - x[j])**3
#           for x[j] <= x <= x[j+1].)

# Function for value input.
def inp(OK, n, x, a):
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
        for i in range(n + 1):
            x.append(float(input(f"x{i}: ")))
        print("Please enter the function values f(x0),...,f(xn): ")
        for j in range(n + 1):
            a.append(float(input(f"f(x{j}): ")))

        OK = True

    return OK, n, x, a


def main():
    # Assign initial variables.
    OK = False
    n = 0
    x = []
    a = []

    # Print introduction and input values.
    print("This is the natural cubic spline interpolation algorithm.")
    OK, n, x, a = inp(OK, n, x, a)

    # Assign separate lists for computation.
    b = [0 for i in range(n + 1)]
    c = [0 for j in range(n + 1)]
    d = [0 for k in range(n + 1)]
    h = []
    α = [0]
    l = []
    μ = []
    z = []

    if OK:
        # STEP 1: Set h.
        for i in range(n):
            h.append(x[i + 1] - x[i])

        # STEP 2: Set α
        for i in range(1, n):
            α.append(
                (3 / h[i] * (a[i + 1] - a[i])) - (3 / h[i - 1] * (a[i] - a[i - 1]))
            )

        # STEP 3: Set l, μ, and z.
        l.append(1)
        μ.append(0)
        z.append(0)
        for i in range(1, n):
            l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * μ[i - 1])
            μ.append(h[i] / l[i])
            z.append((α[i] - h[i - 1] * z[i - 1]) / l[i])
        l.append(1)
        μ.append(0)
        z.append(0)

        # STEP 6: Set c, b, and d.
        for j in range(n - 1, -1, -1):
            c[j] = z[j] - μ[j] * c[j + 1]
            b[j] = ((a[j + 1] - a[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j])) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # STEP 7: Output result.
        print("")
        print("Values for the cubic spline interpolant S(x):")
        print("-" * 55)
        print("a(i)\t\tb(i)\t\tc(i)\t\td(i)")
        print("-" * 55)
        for i in range(n + 1):
            print("{:.5f}\t\t{:.5f}\t\t{:.5f}\t\t{:.5f}".format(a[i], b[i], c[i], d[i]))


if __name__ == "__main__":
    main()
