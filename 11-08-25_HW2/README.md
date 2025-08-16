## 📋Problem 1: Square Each Member in a Nested List

**Question**: Write a program to square each member in a nested list.

**Solution**: [View Code](Problem1.py)

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

squared_list = [[num**2 for num in sublist] for sublist in nested_list]

print("Squared Nested List:", squared_list)
```
### OUTPUT

```
Squared Nested List: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```
## 📋Problem 2: Generating a Nested List Using User Input

**Question**: Write a program to generate a nested list using user input.

**Solution**: [View Code](Problem2.py)

```python
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

nested_list = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(value)
    nested_list.append(row)

print("Generated Nested List:", nested_list)
```
### OUTPUT

```
Enter number of rows: 2
Enter number of columns: 3
Enter element at [0][0]: 1
Enter element at [0][1]: 2
Enter element at [0][2]: 3
Enter element at [1][0]: 4
Enter element at [1][1]: 5
Enter element at [1][2]: 6
Generated Nested List: [[1, 2, 3], [4, 5, 6]]
```
## 📋Problem 3: Create a Tuple Using User Input

**Question**: Write a program to create a tuple using user input.

**Solution**: [View Code](Problem3.py)

```python
elements = input("Enter tuple elements separated by space: ")
tuple_data = tuple(map(int, elements.split()))

print("Created Tuple:", tuple_data)
```
### OUTPUT

```
Enter tuple elements separated by space: 10 20 30 40 50
Created Tuple: (10, 20, 30, 40, 50)
```
## 📋Problem 4: Find Length of Any Tuple

**Question**: Write a program to find length of a tuple.

**Solution**: [View Code](Problem4.py)

```python
tuple = (10, 20, 30, 40, 50)

print("Length of Tuple:", len(tuple))
```
### OUTPUT

```
Length of Tuple: 5
```
## 📋Problem 5: Count Occurrences of an Element in a Tuple

**Question**: Write a program to count the occurrences of an element in a tuple.

**Solution**: [View Code](Problem5.py)

```python
tuple = (1, 2, 3, 2, 4, 2, 5, 2)

element = int(input("Enter element to count: "))
count = tuple.count(element)

print(f"{element} occurs {count} times in the tuple.")
```
### OUTPUT

```
Enter element to count: 2
2 occurs 4 times in the tuple.
```
## 📋Problem 6: Concatenate Two Tuples

**Question**: Write a program to concatenate two tuples.

**Solution**: [View Code](Problem6.py)

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print("Concatenated Tuple:", result)
```
### OUTPUT

```
Concatenated Tuple: (1, 2, 3, 4, 5, 6)
```
## 📋Problem 7: Convert List to Tuple

**Question**: Write a program to convert a list into a tuple.

**Solution**: [View Code](Problem7.py)

```python
list = [10, 20, 30, 40, 50]

my_tuple = tuple(list)

print("Converted Tuple:", my_tuple)
```
### OUTPUT

```
Converted Tuple: (10, 20, 30, 40, 50)
```