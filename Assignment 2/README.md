## 📋Program 1: Squares of Even Numbers

**Question**: From a list, generate a new list of squares of even numbers only.

**Solution**: [View Code](Program_1.py)

```python
list = [1, 2, 3, 4, 5, 6, 7, 8]

# Generate squares of even numbers only
squares = [x ** 2 for x in list if x % 2 == 0 ]

print("The squares of even numbers =",squares)
```
### OUTPUT

```
The squares of even numbers = [4, 16, 36, 64]
```
## 📋Program 2: Sum and Average of List Elements

**Question**: Find the Sum and Average of List Elements.

**Solution**: [View Code](Program_2.py)

```python
list = [10, 20, 30, 40, 50]

total = sum(list)
average = total / len(list)

print("Sum of List Elements:", total)
print("Average of List Elements:", average)
```
### OUTPUT

```
Sum of List Elements: 150
Average of List Elements: 30.0
```
## 📋Program 3: Convert List of Strings to Integers

**Question**: Write a program to convert list of strings to integers.

**Solution**: [View Code](Program_3.py)

```python
string_list = ["1", "2", "3", "4", "5"]

int_list = [int(x) for x in string_list]

print("Converted List:", int_list)
```
### OUTPUT

```
Converted List: [1, 2, 3, 4, 5]
```
## 📋Program 4: Tuple Unpacking

**Question**: Find the tuple from a list of tuples that has the maximum sum of elements.

**Solution**: [View Code](Program_4.py)

```python
tuple = (10, 20, 30, 40, 50)

# Unpacking
a, b, c, d, e = tuple

print("Unpacked Variables : ")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
```
### OUTPUT

```
Unpacked Variables : 
a = 10
b = 20
c = 30
d = 40
e = 50
```
## 📋Program 5: Tuple with Maximum Sum

**Question**: Find the tuple from a list of tuples that has the maximum sum of elements.

**Solution**: [View Code](Program_5.py)

```python
tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]

max_tuple = max(tuples, key=sum)

print("Tuple with maximum sum:", max_tuple)
```
### OUTPUT

```
Tuple with maximum sum: (7, 8)
```
## 📋Program 6: Replace Element in Tuple

**Question**: Tuples are immutable. Replace an element by converting the tuple to a list and back.

**Solution**: [View Code](Program_6.py)

```python
my_tuple = (10, 20, 30, 40, 50)
temp_list = list(my_tuple)

temp_list[2] = 69  # replacing element at index 2
new_tuple = tuple(temp_list)

print("Modified Tuple:", new_tuple)
```
### OUTPUT

```
Modified Tuple: (10, 20, 69, 40, 50)
```