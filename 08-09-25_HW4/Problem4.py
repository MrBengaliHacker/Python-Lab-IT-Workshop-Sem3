import random as rd
import math

# Generate a random number between 1 and 100
n = rd.randint(1, 100)
print("Generated number:", n)

# Check if the number is a perfect square
sqrt_n = math.isqrt(n)  # integer square root of n
if sqrt_n * sqrt_n == n:
  print(n, "is a perfect square.")
else:
  print(n, "is not a perfect square.")
