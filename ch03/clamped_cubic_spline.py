# 3.5 Clamped Cubic Spline
# To construct the cubic spline interpolant S for the function f,
# defined at the numbers x0 < x1 < ... < xn,
# satisfying S'(x[0]) = f'(x[0]) and S'(x[n]) = f'(x[n]);
# Input: n; x[0], x[1],... ,x[n]; a[0] = f(x[0]), a[1] = f(x[1]),... , a[n] = f(x[n]),
#        FPO = f'(x[0]); FPN = f'(x[n]).
# Output: a[j], b[j], c[j], d[j] for j = 0, 1,..., n-1.
#       (Note: S(x) = S[j](x) = a[j] + bj(x - x[j]) + cj(x - x[j])**2 + dj(x - x[j])**3
#           for x[j] <= x <= x[j+1].)

# Function for value input.
def inp(OK, n, x, a, FPO, FPN):
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
        FPO = float(input("Please enter a value for f'(x0): "))
        FPN = float(input("Please enter a value for f'(xn): "))

        OK = True

    return OK, n, x, a, FPO, FPN


def main():
    # Assign initial variables.
    OK = False
    n = 0
    x = []
    a = []
    FPO = 0.0
    FPN = 0.0

    # Print introduction and input values.
    print("This is the clamped cubic spline interpolation algorithm.")
    OK, n, x, a, FPO, FPN = inp(OK, n, x, a, FPO, FPN)

    # Assign separate lists for computation.
    b = [0 for i in range(n + 1)]
    c = [0 for j in range(n + 1)]
    d = [0 for k in range(n + 1)]
    h = []
    α = []
    l = []
    μ = []
    z = []

    if OK:
        # STEP 1: Set h.
        for i in range(n):
            h.append(x[i + 1] - x[i])

        # STEP 2, 3: Set α
        α.append((3 * (a[1] - a[0])) / h[0] - 3 * FPO)
        for i in range(1, n):
            α.append(
                (3 / h[i] * (a[i + 1] - a[i])) - (3 / h[i - 1] * (a[i] - a[i - 1]))
            )
        α.append((3 * FPN - 3 * (a[n] - a[n - 1])) / h[n - 1])

        # STEP 4: Set l[0], μ[0], and z[0].
        l.append(2 * h[0])
        μ.append(0.5)
        z.append(α[0] / l[0])

        # STEP 5: Set l[i], μ[i], and z[i].
        for i in range(1, n):
            l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * μ[i - 1])
            μ.append(h[i] / l[i])
            z.append((α[i] - h[i - 1] * z[i - 1]) / l[i])

        # STEP 6: Set l[n], z[n], and c[n]
        l.append(h[n - 1] * (2 - μ[n - 1]))
        z.append((α[n] - h[n - 1] * z[n - 1]) / l[n])
        c[n] = z[n]

        # STEP 7: Set c, b, and d.
        for j in range(n - 1, -1, -1):
            c[j] = z[j] - μ[j] * c[j + 1]
            b[j] = ((a[j + 1] - a[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j])) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # STEP 8: Output result.
        print("")
        print("Values for the cubic spline interpolant S(x):")
        print("-" * 55)
        print("a(i)\t\tb(i)\t\tc(i)\t\td(i)")
        print("-" * 55)
        for i in range(n + 1):
            print("{:.5f}\t\t{:.5f}\t\t{:.5f}\t\t{:.5f}".format(a[i], b[i], c[i], d[i]))


if __name__ == "__main__":
    main()
