import random as rd

# Generate a random number between 1 and 10
n = rd.randint(1, 10)
print("Generated number:", n)

# Calculate factorial
factorial = 1
for i in range(1, n + 1):
  factorial *= i

print(f"Factorial of {n} is {factorial}")
