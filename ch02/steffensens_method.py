# 2.6 Steffensen's Method
# To find a solution to p = g(p) given an initial approximation p0:
# INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# import the math module
import math


# define the function g(x)
def g(x):
    return math.pow(5.0, -x)


# define function to input values
def inp_vals(OK, p_0, TOL, n_0):
    # set flag for input validation to false
    OK = False
    # check if function has been assigned
    ans = input("Have you defined the function g before starting this program? (Y/N): ")
    if ans == "Y" or ans == "y":
        # input initial approximation p_0
        p_0 = float(input("Please enter an initial approximation P0: "))

        # input tolerance TOL
        OK = False
        while not OK:
            TOL = float(input("Please input a value for the tolerance: "))
            # check that TOL is positive
            if TOL > 0:
                OK = True
            else:
                print("Tolerance must be a positive value.")

        # input maximum number of iterations N0
        OK = False
        while not OK:
            n_0 = int(
                input(
                    "Please input a value for the maximum number of iterations (N0): "
                )
            )
            # check that n_0 is positive
            if n_0 > 0:
                OK = True
            else:
                print("Maximum number of iterations must be a positive integer.")

        # return function values
        return OK, p_0, TOL, n_0
    else:
        print("Terminating program so that function can be defined.")
        return


# define absolute value function
def abs_val(x):
    if x < 0.0:
        return -x
    else:
        return x


# define function to output row of table
def row_outp(n, p_0, p_1, p_2):
    if not isinstance(p_1, str) and not isinstance(p_2, str):
        print("{}\t\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, p_0, p_1, p_2))
    else:
        print("{}\t\t{:.10f}\t{}\t{}\n".format(n, p_0, p_1, p_2))


def main():
    # welcome message
    print("This is Steffensen's method")

    # declare variables with initial values
    OK = False
    p_0 = TOL = 0.0
    n_0 = 0

    OK, p_0, TOL, n_0 = inp_vals(OK, p_0, TOL, n_0)

    # check if output must be table or answer only
    OK = False
    while not OK:
        outp = int(
            input("Would you like to print a table (0) or the answer only (1)? ")
        )
        if outp == 0 or outp == 1:
            OK = True

        # STEP 3: compute p1, p2 with superscript i-1 for first output
        p_1 = g(p_0)
        p_2 = g(p_1)

    # output table heading
    if outp == 0:
        print("-" * 60)
        print("n\t\tp0\t\tp1\t\tp2")
        print("-" * 60)
        row_outp(0, p_0, p_1, p_2)

    if OK:
        # STEP 1: set iterator
        i = 1
        OK = True

        # STEP 2: do Steps 3-6
        while i <= n_0 and OK:
            # STEP 3: compute p1, p2 with superscript i-1
            p_1 = g(p_0)
            p_2 = g(p_1)

            # check for division by 0
            if abs_val(p_2 - (2.0 * p_1) + p_0) < 0:
                print("\nDenominator = 0, method fails.")
                print("Best possible is P2({}) = {:.10f}".format(i, p_2))
                OK = False
            else:
                d = math.pow((p_1 - p_0), 2.0) / (p_2 - (2.0 * p_1) + p_0)

            # compute p0 with superscript i - 1
            p = p_0 - d

            # if table output selected, output row
            if outp == 0:
                p_1 = g(p)
                p_2 = g(p_1)

                # for table output only
                if abs_val(p - p_0) < TOL:
                    row_outp(i, p, "\t", "\t")
                else:
                    row_outp(i, p, p_1, p_2)

                # return to previous values after output
                p_1 = g(p_0)
                p_2 = g(p_1)

            # STEP 4: the procedure was successful
            if abs_val(p - p_0) < TOL:
                print(
                    "\nApproximate solution P = {:.10f}\nNumber of iterations = {}\nTOL = {}\n".format(
                        p, i, TOL
                    )
                )
                OK = False
                return

            # STEP 5: increment iterator
            i += 1

            # STEP 6: update p0
            p_0 = p

        # STEP 7: the procedure was unsuccessful
        if OK:
            print(
                "\nIteration number {} gave approximation {:.10f}, not within tolerance {}.".format(
                    n_0, p, TOL
                )
            )


if __name__ == "__main__":
    main()
