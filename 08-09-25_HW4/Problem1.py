import random as rd

n = rd.randint(1, 100)
print("Generated number:", n)

if n < 2:
  print(n, "is not a prime number.")
else:
  for i in range(2, n):
    if n % i == 0:
      print(n, "is not a prime number.")
      break
  else:
    print(n, "is a prime number.")
