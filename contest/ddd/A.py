import math
t = int(input())

for x in range(t):
  n = int(input())
  a = [1] * n
  if n % 4 == 0:
    a[-1] += 1  

  for k in range(2, n + 1):
    if n % k == 0:  # Check if k divides n
      num_multiples = n // k  # Number of multiples of k in the array
      adjustment = k // math.gcd(k, num_multiples)  # Calculate adjustment

      # Distribute adjustment equally among multiples of k
      for i in range(k, n + 1, k):
        a[i - 1] += adjustment // num_multiples
  
  print(*a)