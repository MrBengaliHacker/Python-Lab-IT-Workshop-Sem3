## 📋Problem 1: Generate Random Number and Check if It Is Prime

**Question**: Generate random number and check if it is prime

**Solution**: [View Code](Problem1.py)

```python
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
```
### OUTPUT

```
Generated number: 36
36 is not a prime number.
```
## 📋Problem 2: Factorial of a Random Number

**Question**: Calculate a factorial by generating a random number.

**Solution**: [View Code](Problem2.py)

```python
import random as rd

# Generate a random number between 1 and 10
n = rd.randint(1, 10)
print("Generated number:", n)

# Calculate factorial
factorial = 1
for i in range(1, n + 1):
  factorial *= i

print(f"Factorial of {n} is {factorial}")
```
### OUTPUT

```
Generated number: 6
Factorial of 6 is 720
```
## 📋Problem 3: Average of 5 Random Numbers

**Question**: Generate 5 random integers and find their average

**Solution**: [View Code](Problem3.py)

```python
import random as rd

# Generate 5 random integers between 1 and 100
numbers = [rd.randint(1, 100) for _ in range(5)]
print("Generated numbers:", numbers)

# Calculate average
average = sum(numbers) / len(numbers)
print("Average:", average)
```
### OUTPUT

```
Generated numbers: [21, 50, 34, 74, 1]
Average: 36.0
```
## 📋Problem 4: Check Perfect Square for a Random Number

**Question**: Take a random number and check if it is a perfect square

**Solution**: [View Code](Problem4.py)

```python
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
```
### OUTPUT

```
Generated number: 41
41 is not a perfect square.
```
## 📋Problem 5: Build a Proper Package with Program and Output

**Question**: Build a proper Python package named `number_utils` that contains useful functions for working with numbers.  
The package should include:

- A module to generate a random number.  
- A module to check if a number is a perfect square.  

Then, write a main program that imports and uses this package to display results.

---

**Solution**:

**📁 Folder Structure**

```
PythonPackageDemo/
│
├── number_utils/
│   ├── __init__.py
│   ├── random_gen.py
│   └── math_check.py
│
└── main.py
```


**File: number_utils/__init__.py**
```python
# This file makes number_utils a package
```
**File: number_utils/random_gen.py**
```python
import random

def generate_random_number(start=1, end=100):
  """Generate a random integer between start and end."""
  return random.randint(start, end)
```
**File: number_utils/math_check.py**
```python
import math

def is_perfect_square(n):
  """Check if n is a perfect square."""
  sqrt_n = math.isqrt(n)
  return sqrt_n * sqrt_n == n
```
**File (in PythonPackageDemo Folder): main.py**
```python
from number_utils.random_gen import generate_random_number
from number_utils.math_check import is_perfect_square

# Generate a random number
n = generate_random_number()
print("Generated number:", n)

# Check if it is a perfect square
if is_perfect_square(n):
  print(n, "is a perfect square.")
else:
  print(n, "is not a perfect square.")
```
### OUTPUT

```
Generated number: 64
64 is a perfect square.
```