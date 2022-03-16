# 6.3 Gaussian Elimination with Scaled Partial Pivoting
# To solve the n x n linear system
#   E1: a(1,1)x1 + a(1,2)x2 + ... + a(1,n)xn = a(1,n+1)
#   E2: a(2,1)x1 + a(2,2)x2 + ... + a(2,n)xn = a(2,n+1)
#    .      .         .                 .         .
#    :      :         :                 :         :
#   En: a(n,1)x1 + a(n,2)x2 + ... + a(n,n)xn = a(n,n+1)
# Input: number of unknowns and equations n; augmented matrix A = [a(i,j)],
#        where 1 <= i <= n and 1 <= j <= n + 1.
# Output: solution x1, x2, ..., xn or message that the linear system has
#         no unique solution.
import numpy as np

def inp(OK, n, A):
  OK = False

  # Input n
  while not OK:
    n = int(input("Please input the number of unkowns and equations (n): "))
    if n <= 0:
      print("Must be a positive integer value.")
    else:
      OK = True

  # Declare A as uninitialized array
  A = np.empty([n, n+1])

  # Fill array coefficients
  OK = False
  while not OK:
    print("Please enter the coefficients for matrix A: ")
    for i in range(n):
      print(f"Row {i+1}:")
      for j in range(n+1):
        A[i, j] = np.double(input(f"A[{i+1}, {j+1}]: "))
    OK = True

  return OK, n, A

def main():
  OK = False
  n = 0
  A = np.empty(0)

  print("This is Gaussian Elimination with Scaled Partial Pivoting.")

  OK, n, A = inp(OK, n, A)
  x = np.empty(n)
  s = np.empty(n)
  for i in range(n):
    s[i] = A[i, 0]

  # Step 1: Initialize variables (no pointer)
  if OK:
    i = 0
    n_n = n - 1
    m = n + 1
    ichg = 0

    # Populate array s with scale factors
    for j in range(n):
      for k in range(n):
        if abs(A[j, k]) > s[j]:
          s[j] = abs(A[j, k])
      if s[j] == 0:
        OK = False
    
    # Step 2: Elimination proess
    while OK and i < n_n:
      NROW = i
      # Step 3: Determine NROW from max|(A[j,i])|
      for p in range(i, n):
        max = abs(A[i, i]) / s[i]
        for j in range(i, n):
          if abs(A[j, i]) / s[j] > max:
            max = abs(A[j, i]) / s[j]
        if abs(A[p, i]) / s[p] == max:
          NROW = p

      # Step 4: Check for failure
      if A[NROW, i] == 0:
        OK = False
      else:
        # Step 5: Row interchange
        if NROW != i:
          tempA = np.array(A[NROW, :])
          A[NROW, :] = A[i, :]
          A[i, :] = tempA
          temps = s[NROW]
          s[NROW] = s[i]
          s[i] = temps
          ichg += 1

        # Step 6: Loop Steps 7 and 8
        for j in range(i+1, n):
          # Step 7: Set m(j,i) = a(j,i)/a(i,i).
          x_m = A[j, i] / A[i, i]
          
          # Step 8: Perform (Ej - m(j,i)*Ei) -> (Ej)
          A[j, :] = A[j, :] - (x_m * A[i, :])
          A[j, i] = 0
      i += 1
    if OK:
      # Step 9: If a(n,n) = 0, terminate.
      if A[n-1, n-1] == 0:
        print('No unique solution exists.')
        OK = False
      else:
        # Step 10: Start backward substitution.
        x[n-1] = A[n-1, m-1] / A[n-1, n-1]

        # Step 11: Determine xi
        for i in range(n-2, -1, -1):
          sum = 0
          for j in range(i+1, n):
            sum += A[i, j] * x[j]
          x[i] = (A[i, n] - sum) / A[i, i]

        # Step 12: Procedure completed successfully
        print("\nAfter Gaussian Elimination with Scaled Partial Pivoting,")
        print(f"matrix A = \n{A}")
        print(f"Solution vector x = \n{x}")
        print(f"Number of row interchanges: {ichg}")
    else:
      print("No unique solution exists.")

# Call main function
main()