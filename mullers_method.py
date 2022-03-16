# 2.8 Müller's Method
# To find a solution to f(x) = 0 given initial approximations p0, p1, and p2:
# INPUT initial approximations p0, p1, p2; tolerance TOL;
# maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# import the math module
import math
import cmath


# define value input function
def val_inp(OK, n, a, x, TOL, m):
  # input degree of polynomial
  OK = False
  while not OK:
    n = int(input("What is the degree of the polynomial? "))

    if n <= 0:
      print("Must be a positive integer value.")
    else:
      OK = True

  # create lists of coefficients and initial approximations
  a = [None for i in range(n + 1)]
  x = [0.0 for j in range(4)]

  # populate list with coefficients
  print("Please enter the coefficients in ascending order.")
  for i in range(n + 1):
    a[i] = float(input("Please enter a value for coefficient a{}: ".format(i)))
  OK = True

  # check for errors
  if a[n] == 0:
    print("Leading coefficient cannot be 0, error in input.")
    OK = False
  elif n == 1:
    p = -a[0] / a[1]
    print("Polynomial is linear: root is {}".format(p))
    OK = False
  
  if OK:
    # input tolerance TOL
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
      m = int(input("Please enter a value for the maximum number of iterations (N0): "))

      if m <= 0:
        print("N0 must be a positive value.")
      else:
        OK = True

  # input initial approximations p0 and p1
  for i in range(3):
    x[i] = float(input("Please enter initial approximation p{}: ".format(i)))

  # return values if function has been defined 
  if OK:
    return OK, n, a, x, TOL, m


# define function to output row of table
def row_outp(i, p, f_p):
  print("{}\t\t{:.10f}\t{:.10f}\n".format(i, p, f_p))


def main():
  # assign variables to initial values
  OK = False
  a = x = f = h = del1 = []
  TOL = del2 = 0.0
  n = m = 0

  # print introduction
  print("This is Müller's method.")

  # input values for p_0, p_1, TOL, n_0
  OK, n, a, x, TOL, m = val_inp(OK, n, a, x, TOL, m)

  # check if output must be table or answer only
  OK = False
  while OK == False:
    outp = int(input("Would you like to print a table (0) or the answer only (1)? "))

    if outp == 0 or outp == 1:
      OK = True

  # populate empty lists
  f = [0.0 for i in range(4)]
  h = [0.0 for j in range(3)]
  del1 = [0.0 for k in range(2)]

  # evaluate f(x_i) using Horner's Method and save in the list f
  for i in range(3):
    f[i] = a[n]
    for j in range(n-1, -1, -1):
      f[i] = (f[i] * x[i]) + a[j]

  # variable ISW is used to note a switch to complex arithmetic
  # ISW = 0 means real arithmetic, and ISW = 1 means complex arithmetic
  ISW = 0

  # STEP 1: function values and iterator
  if OK:
    h[0] = x[1] - x[0]
    h[1] = x[2] - x[1]
    del1[0] = (f[1] - f[0]) / h[0]
    del1[1] = (f[2] - f[1]) / h[1]
    del2 = (del1[1] - del1[0]) / (h[1] + h[0])
    i = 3
    OK = True

    # STEP 2: while i <= N0 do steps 3-7
    while i <= m and OK:

      # STEP 3: compute b and D (may require complex arithmetic)
      b = del1[1] + (h[1] * del2)
      D = (b*b) - (4.0 * f[2] * del2)

      # test to see if complex arithmetic needed
      if ISW == 0 and D < 0.0: # complex arithmetic
        ISW = 1
        # output table heading
        if i == 3:
          if outp == 0:
            print('-' * 75)
            print("\t\tp0 = {}, p1 = {}, p2 = {}".format(x[0], x[1], x[2]))
            print('-' * 75)
            print("i\t\tp_i\t\t\t\tf(p_i)")
            print('-' * 75)
        for i in range(4):
          f[i] = complex(f[i], 0.0)
          x[i] = complex(x[i], 0.0)
        for j in range(3):
          h[j] = complex(h[j], 0.0)
        for k in range(2):
          del1[k] = complex(del1[k], 0.0)
        del2 = complex(del2, 0.0)


      # output table heading
      if i == 3:
        if ISW == 0 and outp == 0:
          print('-' * 45)
          print("\tp0 = {}, p1 = {}, p2 = {}".format(x[0], x[1], x[2]))
          print('-' * 45)
          print("i\t\tp_i\t\tf(p_i)")
          print('-' * 45)

      # test to see if straight line
      if abs(del2) <= 0.0:
        # straight line - test to see if horizontal line
        if abs(del1[1]) <= 0.0:
          print("Horizontal Line\n")
          OK = False
        else:
        # straight line but not horizontal
          x[3] = (f[2] - (del1[1] * x[2])) / del1[1]
          h[2] = x[3] - x[2]
      else:
        # not straight line
        if ISW == 1:
          D = cmath.sqrt(D)
        else:
          D = math.sqrt(D)

        # STEP 4: check |b - D|
        if abs(b - D) < abs(b + D):
          E = b + D
        else:
          E = b - D

        # STEP 5: set h and p
        h[2] = ((-2.0) * f[2]) / E
        x[3] = x[2] + h[2]

      if OK:
        # Evaluate F using Horner's Method and save in the list f
        f[3] = a[n]
        for j in range(n-1, -1, -1):
          f[3] = (f[3] * x[3]) + a[j]

        # if table output selected, output row
        if outp == 0:
          row_outp(i, x[3], f[3])

        # STEP 6: check if procedure was successful
        if abs(h[2]) < TOL:
          print("\nApproximate solution P = {:.10f}\nf(P) = {:.10}\nNumber of iterations = {}\nTOL = {}\n".format(x[3], f[3], i, TOL))
          OK = False
          return
        else:
          # STEP 7: prepare for next iteration
          for j in range(2):
            h[j] = h[j+1]
            x[j] = x[j+1]
            f[j] = f[j+1]
          x[2] = x[3]
          f[2] = f[3]
          del1[0] = del1[1]
          del1[1] = (f[2] - f[1]) / h[1]
          del2 = (del1[1] - del1[0]) / (h[1] + h[0])
      # STEP 7 continued
      i += 1

    # STEP 8: the procedure was unsuccessful
    if (i > m) and OK:
      print("\nIteration number {} gave approximation {:.10f}, with f(P) = {:.10f}\nnot within tolerance {}.".format(i, x[3], f[3], TOL))


# call main function
main()