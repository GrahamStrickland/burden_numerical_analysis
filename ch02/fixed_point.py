# 2.2 Fixed Point Iteration
# To find a solution to p = g(p) given an initial approximation p0:
# INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# import the math module
import math


# define the function g(x)
def g(x):
  return 2.0 * math.exp(-x)


# define function to input values
def inp_vals(OK, p_0, TOL, n_0):
  # set flag for input validation to false
  OK = False
  # check if function has been assigned
  ans = input("Have you defined the function g before starting this program? (Y/N): ")
  if ans == 'Y' or ans == 'y':
    # input initial approximation p_0
    p_0 = float(input("Please enter an initial approximation P0: "))

    # input tolerance TOL
    OK = False
    while OK == False:
      TOL = float(input("Please input a value for the tolerance: "))
      # check that TOL is positive
      if TOL > 0:
        OK = True
      else:
        print("Tolerance must be a positive value.")

    # input maximum number of iterations N0
    OK = False
    while OK == False:
      n_0 = int(input("Please input a value for the maximum number of iterations (N0): "))
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


# define function to output row of table
def row_outp(n, p):
  print("{}\t\t{:.10f}\n".format(n, p))


def main():
  # welcome message
  print("This is the fixed-point iteration algorithm")

  # declare variables with initial values
  OK = False
  p_0 = TOL = 0.0
  n_0 = 0

  OK, p_0, TOL, n_0 = inp_vals(OK, p_0, TOL, n_0)
  
  # check if output must be table or answer only
  OK = False
  while OK == False:
    outp = int(input("Would you like to print a table (0) or the answer only (1)? "))
    if outp == 0 or outp == 1:
      OK = True

    # output table heading
    if outp == 0:
      print('-' * 27)
      print("n\t\tP")
      print('-' * 27)
      row_outp(0, p_0)
  
  if OK:
    # STEP 1: set iterator
    i = 1
    OK = True
    
    # STEP 2: do Steps 3-6
    while i <= n_0 and OK:
      # STEP 3: compute p_i
      p = g(p_0)

      # if table output selected, output row
      if outp == 0:
        row_outp(i, p)
      
      # STEP 4: the procedure was successful
      if abs(p - p_0) < TOL:
        print("\nApproximate solution P = {:.10f}\nNumber of iterations = {}\nTOL = {}\n".format(p, i, TOL))
        OK = False
        return
      
      # STEP 5: increment iterator
      i += 1

      # STEP 6: update p_0
      p_0 = p

    # STEP 7: the procedure was unsuccessful
    if OK:
      print("\nIteration number {} gave approximation {:.10f}, not within tolerance {}.".format(n_0, p, TOL))


main()