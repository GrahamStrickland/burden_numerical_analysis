# 2.2 Fixed Point Iteration
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


def fixed_point(function: Callable[[float], float],
                p0: float, tol: float, n0: int,
                file: TextIO = None, table_output: bool = False) -> float:
  """To find a solution to p = g(p) given an initial approximation p0:
  INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
  OUTPUT approximate solution p or message of failure.
  """
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

def bisect(function: Callable[[float], float],
           a: float, b: float, tol: float, n0: int,
           file: TextIO = None, table_output: bool = False) -> float:
  """To find a solution to f(x) = 0 given the continuous function f on the interval
  [a, b], where f(a) and f(b) have opposite signs:
  INPUT endpoints a, b; tolerance tol; maximum number of iterations n0.
  OUTPUT approximate solution p or message of failure.
  """
  if table_output:
    # output table heading
    output_string = f"{'-'*80}\n\t\ta\t\tb\t\tP\t\tf(P)\n{'-'*80}"
    if not file:
      print(output_string)
    else:
      file.write(output_string + '\n')

  # STEP 1: set iterator
  i: int = 1
  f_a: float = function(a)
  p: float = 0.0
  f_p: float = 0.0

  # STEP 2: while i < N0 do steps 3-6
  while i <= n0:
    # STEP 3: compute p_i
    c: float = (b - a) / 2.0
    p = a + c
    f_p = function(p)

    # if table output selected, output row
    if table_output:
      row_output(i, a, b, p, f_p, file)

    # STEP 4: procedure completed successfully
    if abs(f_p) == 0.0 or c < tol:
      output_string = cleandoc("""\
                Approximate solution P = {:.10f}
                f(P) = {:.10}
                Number of iterations = {}
                TOL = {}
                """.format(p, f_p, i, tol))
      if table_output:
        output_string = '-' * 80 + '\n' + output_string
      if not file:
        print(output_string)
      else:
        file.write(output_string)
      return p

    # STEP 5: increment iterator to continue running algorithm
    i += 1

    # STEP 6: compute a_i and b_i
    if f_a * f_p > 0.0:
      a = p
      f_a = f_p
    else:
      b = p   # f(a) is unchanged

  # STEP 7: method failed, output result
  output_string = cleandoc("""\
        Method failed after {} iterations with approximation {:.10f}
        and f(P) = {:.10f} not within tolerance {}.
        """.format(n0, p, f_p, tol))
  if table_output:
    output_string = '-' * 80 + '\n' + output_string
  if not file:
    print(output_string)
  else:
    file.write(output_string)
  return p


def row_output(n: int, a: float, b: float, p: float, f_p: float,
               file: TextIO) -> None:
  """Function to output row of table."""
  string = "{}\t\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n".format(n, a, b, p, f_p)
  if not file:
    print(string)
  else:
    file.write(string)
