# 2.1 Bisection
# To find a solution to f(x) = 0 given the continuous function f on the interval [a, b], where f(a) and f(b) have opposite signs:
# INPUT endpoints a, b; tolerance TOL; maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# import the math module
import math


# define function f(x)
def f(x):
  return 2.0 - (x * math.exp(x))


def inp_vals(OK, a, b, f_a, f_b, TOL, n_0):
  # check if function has been assigned
  OK = False
  ans = input("Have you defined the function f before starting this program? (Y/N): ")
  if ans == 'Y' or ans == 'y':
    OK = True

    OK = False
    while OK == False:
      # enter amount for lower and upper bounds (a and b)
      a = float(input("Please enter a value for the lower bound (a): "))
      b = float(input("Please enter a value for the upper bound (b): "))

      # check that b != a
      if b == a:
        print("a and b cannot have the same value.")
      else:
        OK = True

      # if b < a, reverse order of a and b
      if b < a:
        x = a
        a = b
        b = x

      # define f(a) and f(b)
      f_a = f(a)
      f_b = f(b)

      # check that f(a) and f(b) have different signs
      if OK == True:
        OK = False
        if f_a * f_b > 0.0:
          print("f(a) and f(b) cannot have the same sign.")
        else:
          OK = True

    OK = False
    while OK == False:
      # input value for tolerance
      TOL = float(input("Please input a value for the tolerance: "))

      # check that TOL > 0
      if TOL <= 0.0:
        print("Tolerance must be a positive number.")
      else:
        OK = True

    OK = False
    while OK == False:
      # input value for maximum number of iterations
      n_0 = int(input("Please input a value for the maximum number of iterations (N0): "))

      # check that N0 > 0
      if n_0 <= 0:
        print("Maximum number of iterations must be a positive integer.")
      else:
        OK = True

    # return values for function
    return OK, a, b, f_a, f_b, TOL, n_0
  else: # if answer is not yes, terminate program
    print("Terminating program so that functions can be defined.")
    return


# define function to output row of table
def row_outp(n, a, b, p, f_p):
  print("{}\t\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, a, b, p, f_p))


# define main function
def main():
  # declare initial values for variables
  OK = False
  a = b = f_a = f_b = TOL = 0.0
  n_0 = 0

  # print introduction
  print("This is the Bisection Algorithm")

  # input values
  OK, a, b, f_a, f_b, TOL, n_0 = inp_vals(OK, a, b, f_a, f_b, TOL, n_0)

  # check if output must be table or answer only
  OK = False
  while OK == False:
    outp = int(input("Would you like to print a table (0) or the answer only (1)? "))
    if outp == 0 or outp == 1:
      OK = True

  # output table heading
  if outp == 0:
    print('-' * 80)
    print("n\t\ta\t\tb\t\tP\t\tf(P)")
    print('-' * 80)

  if OK:
    # STEP 1: set iterator
    i = 1

    # STEP 2: while i < N0 do steps 3-6
    while i < n_0:
      # STEP 3: compute p_i
      c = (b - a)/2.0
      p = a + c
      f_p = f(p)

      # if table output selected, output row
      if outp == 0:
        row_outp(i, a, b, p, f_p)

      # STEP 4: procedure completed successfully
      if abs(f_p) < 0.0 or c < TOL:
        print("\nApproximate solution P = {:.10f}\nf(P) = {:.10}\nNumber of iterations = {}\nTOL = {}\n".format(p, f_p, i, TOL))
        OK = False
        return
      
      # STEP 5: increment iterator to continue running algorithm
      i += 1

      # STEP 6: compute a_i and b_i
      if f_a * f_p > 0.0:
        a = p
        f_a = f_p
      else:
        b = p # f(a) is unchanged
        f_b = f_p

    # STEP 7: method failed, output result
    if OK:
        print("\nIteration number {} gave approximation {:.10f}, with f(P) = {:.10f} not within tolerance {}.".format(n_0, p, f_p, TOL))


# call main function
main()