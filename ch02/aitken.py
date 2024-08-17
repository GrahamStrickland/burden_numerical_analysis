# Aitken's delta-squared method
# INPUT: pn, pn+1, pn+2
# OUTPUT: pn^
# input the math module
import math


# define function for aitken's delta-squared method
def delta_squared(p, p1, p2):
    return p - (math.pow((p1 - p), 2) / (p2 - (2 * p1) + p))


def main():
    # introduction message
    print("This is Aitken's delta-squared method.")

    # input pn, pn+1, and pn+2
    pn = float(input("Please enter a value for pn: "))
    pn_1 = float(input("Please enter a value for pn+1: "))
    pn_2 = float(input("Please enter a value for pn+2: "))

    # call function to calculate pn^
    p = delta_squared(pn, pn_1, pn_2)

    # print value of pn^
    print("pn^ = {:.10f}".format(p))


if __name__ == "__main__":
    main()
