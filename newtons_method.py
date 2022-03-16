# 2.3 Newton's Method
# To find a solution to f(x) = 0 given an initial approximation p0:
# INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
import math


# define function f(x)
def f(x):
  return 2.0 - (x * math.exp(x))


# define derivative of f(x), function f'(x)
def fP(x):
  return  -(math.exp(x) * (x + 1.0))


# define function to input values
def inp_vals(OK, p_0, TOL, n_0):
  # set flag for input validation to false
  OK = False

  # check that function and derivative have been defined
  ans = input("Have the functions f(x) and its derivative f'(x) been defined? (Y/N) ")

  if ans == 'Y' or ans == 'y':
    while OK == False:
      # input initial approximation p0
      p_0 = float(input("Please input the initial approximation (p0): "))

      # input TOL and check for positive value
      TOL = float(input("Please input the error tolerance (TOL): "))
      if TOL <= 0.0:
        print("TOL must be a positive value.")
      else:
        OK = True

      # input maximum number of iterations and check for positive value
      OK = False
      n_0 = int(input("Please input the maximum number of iterations (N0): "))
      if n_0 <= 0:
        print("N0 must be a positive integer.")
      else:
        OK = True

    # return values if function has been defined
    if OK:
      return OK, p_0, TOL, n_0

  # terminate program if function has not been defined  
  else:
    print("Terminating program so that functions can be defined.")
    return


# define function to output row of table
def row_outp(n, p):
  print("{}\t\t{:.10f}\n".format(n, p))


# define main function
def main():
  # declare variables with temporary values
  OK = False
  p_0 = TOL = 0.0
  n_0 = 0

  # print introduction
  print("This is Newton's method")

  # call input function to input values
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
    f_0 = f(p_0)
    # STEP 1: set i = 1
    i = 1

    # STEP 2: while i <= N0 do steps 3-6
    while i <= n_0 and OK:
      # STEP 3: Compute p_i
      fP_0 = fP(p_0)
      d = f_0 / fP_0

      # STEP 6: update p0
      p_0 = p_0 - d
      f_0 = f(p_0)

      # if table output selected, output row
      if outp == 0:
        row_outp(i, p_0)

      # STEP 4: if p - p0 < TOL then the procedure was successful
      if abs(d) < TOL:
        print("\nApproximate solution P = {:.10f}\nf(P) = {:.10}\nNumber of iterations = {}\nTOL = {}\n".format(p_0, f_0, i, TOL))
        OK = False
        return

      # STEP 5: increment iterator
      i += 1

    # STEP 7: The procedure was unsuccessful
    if OK:
      print("\nIteration number {} gave approximation {:.10f}, with f(P) = {:.10f} not within tolerance {}.".format(n_0, p_0, f_0, TOL))


main()