## Build in function in math module

**floor(x)**: The math.floor() function rounds a number downwards to the nearest integer, ignoring the decimal part. It always returns the largest integer less than or equal to x.

**Example**: [View Code](Example1.py)

```python
import math
print(math.floor(12.7))
print(math.floor(-4.8))
```
### OUTPUT

```
12
-5
```

**pow(x, y)**: The math.pow() function returns x raised to the power y (x^y). The result is always returned as a floating-point number, even if both arguments are integers.

**Example**: [View Code](Example2.py)

```python
import math
print(math.pow(2, 5))
```
### OUTPUT

```
32.0
```

**fabs(x)**: The math.fabs() function returns the absolute (non-negative) value of a number as a float. Unlike the built-in abs(), it always returns a floating-point result.

**Example**: [View Code](Example3.py)

```python
import math
print(math.fabs(-15))    # Converts to positive 15.0
print(math.fabs(25))     # Already positive
```
### OUTPUT

```
15.0
25.0
```

**factorial(n)**: The math.factorial() function returns the factorial of n, which is the product of all positive integers up to n. Factorial is only defined for non-negative integers.

**Example**: [View Code](Example4.py)

```python
import math
print(math.factorial(5))   # 5! = 5×4×3×2×1
```
### OUTPUT

```
120
```

**cos(x)**: The math.cos() function returns the cosine of x, where x is given in radians. To work with degrees, convert them using math.radians().

**Example**: [View Code](Example5.py)

```python
import math
print(math.cos(math.pi/3))        # cos(60°) = 0.5
print(math.cos(math.radians(60))) # Same result
```
### OUTPUT

```
0.5000000000000001
0.5000000000000001
```

**tan(x)**: The math.tan() function returns the tangent of x, where x is given in radians. If you want degrees, convert them with math.radians().

**Example**: [View Code](Example6.py)

```python
import math
print(math.tan(math.pi/4))        # tan(45°) = 1
print(math.tan(math.radians(45))) # Same result
```
### OUTPUT

```
0.9999999999999999
0.9999999999999999
```