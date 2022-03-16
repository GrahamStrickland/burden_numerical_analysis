# 2.4 Secant Method
# To find a solution to f(x) = 0 given initial approximations p0 and p1:
# INPUT initial approximations p0, p1; tolerance TOL;
# maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# import the math module
import math


# define function f(x)
def f(x):
  return math.log(x**2.0 + 1.0) - math.exp(0.4 * x) * math.cos(math.pi * x)



# define value input function
def val_inp(OK, p_0, p_1, TOL, n_0):
  # set flag for input validation to False
  OK = False

  # check that the function f(x) has been defined
  ans = input("Has the function f(x) been defined in the program? (Y/N) ")

  if ans == 'Y' or ans == 'y':
    while OK == False:
      # input initial approximations p0 and p1
      p_0 = float(input("Please input the first initial approximation (p0): "))
      p_1 = float(input("Please input the second initial approximation (p1): "))
      
      if p_0 == p_1:
        print("p0 cannot be equal to p1.")
      else:
        OK = True

    # input tolerance TOL
    OK = False
    while OK == False:
      TOL = float(input("Please input a value for the tolerance (TOL): "))
      
      if TOL <= 0.0:
        print("TOL must be a positive value.")
      else:
        OK = True

    # input maximum number of iterations
    OK = False
    while OK == False:
      n_0 = int(input("Please input a value for the maximum number of iterations (N0): "))

      if n_0 <= 0:
        print("N0 must be a positive value.")
      else:
        OK = True

    # return values if function has been defined 
    if OK:
      return OK, p_0, p_1, TOL, n_0

  # terminate program if function has not been defined
  else:
    print("Terminating program so that function f(x) can be defined.")
    return


# define function to output row of table
def row_outp(n, p):
  print("{}\t\t{:.10f}\n".format(n, p))


def main():
  # assign variables to zero values
  OK = False
  p_0 = p_1 = TOL = 0.0
  n_0 = 0

  # print introduction
  print("This is the Secant method.")

  # input values for p_0, p_1, TOL, n_0
  OK, p_0, p_1, TOL, n_0 = val_inp(OK, p_0, p_1, TOL, n_0)

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
      row_outp(1, p_1)
  
  # STEP 1: set iterator and function values q0 and q1
  if OK:
    i = 2
    q_0 = f(p_0)
    q_1 = f(p_1)

    # STEP 2: while i <= N0 do steps 3-6
    while i <= n_0 and OK:
      # STEP 3: compute p_i
      p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)

      # if table output selected, output row
      if outp == 0:
        row_outp(i, p)

      # STEP 4: check if procedure was successful
      f_p = f(p)
      if abs(p - p_1) < TOL:
        print("\nApproximate solution P = {:.10f}\nf(P) = {:.10}\nNumber of iterations = {}\nTOL = {}\n".format(p, f_p, i, TOL))
        return
      else:
        # STEP 5: increment iterator
        i += 1

        # STEP 6: update p_0, q_0, p_1, q_1
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f_p

    # STEP 7: the procedure was unsuccessful
    if OK:
      print("\nIteration number {} gave approximation {:.10f}, with f(P) = {:.10f}\nnot within tolerance {}.".format(n_0, p, f_p, TOL))


# call main function
main()