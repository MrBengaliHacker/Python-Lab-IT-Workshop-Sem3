## 📋Program : Hello World

**Question**: Write Python program to print " Hello World"

**Solution**: [View Code](Program_1.py)

```python
print("Hello World")
```
### OUTPUT

```
Hello World
```
## 📋Program : Sum of Two Numbers

**Question**: Write a program to take 2 values from user ,sum them, print the result.

**Solution**: [View Code](Program_2.py)

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("The sum is:", a + b)
```
### OUTPUT

```
Enter first number: 12.5
Enter second number: 7.5
The sum is: 20.0
```
## 📋Program : Demonstrate id(), type(), sep, end, |, &, ^, <<, >>

**Question**: Write program to implement id(), type(),sep,end, | , &&, ^ , << ,>>

**Solution**: [View Code](Program_3.py)

```python
x = 10
y = 12

# id() and type()
print("ID of x:", id(x))
print("Type of x:", type(x))
print("ID of y:", id(y))
print("Type of y:", type(y))

# sep and end
print("Hello", "Friend", sep="-", end=" :) \n")


# Bitwise operators
print("x | y  =", x | y)  # Bitwise OR
print("x & y =", x & y)   # Bitwise AND
print("x ^ y  =", x ^ y)  # Bitwise XOR

print("x << 1 =", x << 1) # Bitwise Left Shift
print("x >> 1 =", x >> 1) # Bitwise Right Shift
```
### OUTPUT

```
ID of x: 140735979014872
Type of x: <class 'int'>
ID of y: 140735979014936
Type of y: <class 'int'>
Hello-Friend :)
x | y  = 14
x & y = 8
x ^ y  = 6
x << 1 = 20
x >> 1 = 5
```
## 📋Program : Net Amount Payable with Discount on Electronic Goods

**Question**:  Write a program for net amount payable on purchasing Electronic goods

- If Cost >= 50000 discount : 15%
- If Cost in between 30000 to 50000 discount: 10%
- If Cost in between 20000 to 30000 discount : 5%

**Solution**: [View Code](Program_4.py)

```python
cost = float(input("Enter the cost of the electronic item: ₹"))

if cost >= 50000:
    discount = 0.15
elif 30000 <= cost < 50000:
    discount = 0.10
elif 20000 <= cost < 30000:
    discount = 0.05
else:
    discount = 0.0

discount_amount = cost * discount
net_amount = cost - discount_amount

print("Discount Applied: ₹", discount_amount)
print("Net Amount Payable: ₹", net_amount)
```
### OUTPUT

```
Enter the cost of the electronic item: ₹40000
Discount Applied: ₹ 4000.0
Net Amount Payable: ₹ 36000.0
```
```
Enter the cost of the electronic item: ₹15000
Discount Applied: ₹ 0.0
Net Amount Payable: ₹ 15000.0
```