# 10.1 Newton's Method for Systems
# To approximate the solution of the nonlinear system F(x) = 0,
# given an initial approximation x:
# Input: number n of equations and unknowns; 
#        initial approximation x = (x1,...,xn); tolerance TOL;
#        maximum number of iterations N.
# Output: approximate solution x = (x1,...,xn) or a message that
#         the number of iterations was exceeded.
import numpy as np
from numpy import linalg

def inp(OK, n, x, TOL, N):
  # set flag for input validation to false
  OK = False

  # check that function and derivative have been defined
  print("Has the function F been defined and have the partial ")
  print("derivatives been defined as follows:")
  print("1. def F(i, x):")
  print("      where i is the number of the component function;\n")
  print("2. function P:  def P(i, j, x)")
  print("      where i is the number of the component function")
  print("      and j is the number of the variable with respect")
  print("      to which partial differentiation is performed;")
  ans = input("Answer Y or N: ")

  if ans == 'Y' or ans == 'y':
    # Input n
    while not OK:
      n = int(input("Please input the number of unkowns and equations (n): "))
      if n <= 0:
        print("Must be a positive integer value.")
      else:
        OK = True

    # Declare x as uninitialized array
    x = np.empty(n)

    # Input approximation x
    OK = False
    while not OK:
      print("Please enter the initial approximations for x: ")
      for i in range(n):
        x[i] = np.double(input(f"x[{i+1}]: "))
      OK = True

      # Input tolerance TOL
      OK = False
      while not OK:
        TOL = float(input("Please input a value for the tolerance (TOL): "))
        
        if TOL <= 0.0:
          print("TOL must be a positive value.")
        else:
          OK = True

      # input maximum number of iterations
      OK = False
      while OK == False:
        N = int(input("Please enter a value for the maximum number of iterations (N): "))

        if N <= 0:
          print("N0 must be a positive value.")
        else:
          OK = True
    
    return OK, n, x, TOL, N
  else:
    print("Terminating program so that functions can be defined.")
    return


# Change function F for a new problem
def F(i, x):
  if i == 0:
    return x[0]**2 + x[1]**2 + x[2]**2 - 1
  elif i == 1:
    return x[0]**2 + x[2]**3 - 0.25
  elif i == 2:
    return x[0]**2 + x[1]**2 - (4 * x[0])
  else:
    print("Error - incorrect component function reference")
    return


# P is the Jacobian Matrix J(X)
def P(i, j, x):
  if i == 0:
    if j == 0:
      return 2 * x[0]
    elif j == 1:
      return 2 * x[1]
    elif j == 2:
      return 2 * x[2]
    else:
      pass
  elif i == 1:
    if j == 0:
        return 2 * x[0]
    elif j == 1:
      return 0
    elif j == 2:
      return 3 * x[2]**2
    else:
      pass
  elif i == 2:
    if j == 0:
      return (2 * x[0]) - 4
    elif j == 1:
      return 2 * x[1]
    elif j == 2:
      return 0
    else:
      pass
  else:
    print("Error - incorrect component function reference")
    return

# Main function
def main():
  # Declare initial variables
  OK = False
  n = 0
  x = np.empty(0)
  TOL = 0.0
  N = 0

  # Introduction and input
  print("This is Newton's Method for Systems.")

  OK, n, x, TOL, N = inp(OK, n, x, TOL, N)
  f_x = np.zeros(n)
  y = np.zeros(n)
  j_x = np.zeros([n,n])

  if OK:
    # STEP 1: Set k = 1.
    k = 1

    # STEP 2: While (k <= N) do Steps 3-7.
    while k <= N and OK:
      # STEP 3: Calculate F(x) and J(x).
      for i in range(n):
        f_x[i] = F(i, x)
        for j in range(n):
          j_x[i,j] = P(i,j,x)

      # STEP 4: Solve the n x n linear system J(x)y = -F(x).
      y = linalg.solve(j_x, -f_x)

      # STEP 5: Set x.
      x = x + y

      # STEP 6: If ||y|| < TOL, the procedure was successful.
      norm = abs(y[0])
      for i in range(n):
        if abs(y[0]) > norm:
          norm = abs(y[0])
      print(f"k = {k}, x = {x}")
      if norm < TOL:
        print(f"The procedure was successful after {k} iterations.")
        print(f"||y|| = {norm}, < TOL = {TOL}")
        OK = False

      # STEP 7: Set k = k + 1.
      k = k + 1

    # STEP 8: The procedure was unsuccessful.
    if OK:
      print(f"Procedure does not converge in {N} iterations.")
      OK = False

main()