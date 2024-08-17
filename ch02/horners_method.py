# 2.7 Horner's Method
# To evaluate the polynomial
# p(x) = a(n) * x^n + a(n-1) * x^(n-1) + ... + a(1) * x + a(0)
# and its derivative p'(x) at x = x0;
# INPUT degree n; coefficients a-0, a1,...,an; x0
# OUTPUT y = P(x0); z = P'(x0)

# define input function for input values
def inp_vals(OK, deg, coeffs, x_0):
    # input degree of polynomial
    OK = False
    while not OK:
        deg = int(input("What is the degree of the polynomial? "))

        if deg <= 0:
            print("Must be a positive integer value.")
        else:
            OK = True

    # create list of coefficients
    coeffs = [None for x in range(deg + 1)]

    # populate list with coefficients
    print("Please enter the coefficients in ascending order.")
    for i in range(deg + 1):
        coeffs[i] = float(input("Please enter a value for coefficient a{}: ".format(i)))

    # input value for x0
    x_0 = float(input("Please enter a value for x0: "))

    OK = True
    return OK, deg, coeffs, x_0


# define main function
def main():
    # assign initial values for variables
    OK = False
    deg = 0
    coeffs = []
    x_0 = 0.0

    # print introduction
    print("This is Horner's method.")

    # call input function to input values
    OK, deg, coeffs, x_0 = inp_vals(OK, deg, coeffs, x_0)

    # STEP 1 compute bn for P, b(n-1) for Q
    y = coeffs[deg]
    if deg == 0:
        z = 0
    else:
        z = coeffs[deg]

    # STEP 2 compute bj for P, b(j-1) for Q
    for i in range(deg - 1, 0, -1):
        y = (x_0 * y) + coeffs[i]
        z = (x_0 * z) + y

    # STEP 3 compute b0 for P
    if deg != 0:
        y = (x_0 * y) + coeffs[0]

    # STEP 4 outpute final result
    print("\nCoefficients of polynomial P: ")
    for i in range(deg + 1):
        print("Coefficient = {}, exponent = {}".format(coeffs[i], i))
    print("P({}) = {}".format(x_0, y))
    print("P'({}) = {}".format(x_0, z))


if __name__ == "__main__":
    main()
