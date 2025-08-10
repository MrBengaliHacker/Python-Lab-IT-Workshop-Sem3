## 📋Problem 1: Sum of All Elements in a List

**Question**: Write a program to find the sum of all the elements in a list.

**Solution**: [View Code](Problem1.py)

```python
# Define a list of numbers
list = [10, 20, 30, 40, 50]

# Using built-in sum() function
total = sum(list)

# Output the result
print("The sum of all elements in the list is:", total)
```
### OUTPUT

```
The sum of all elements in the list is: 150
```
## 📋Problem 2: Maximum Element in a List

**Question**: Write a program to find the maximum elements in a list.

**Solution**: [View Code](Problem2.py)

```python
# Define a list of numbers
list = [10, 20, 30, 40, 50]

# Using built-in max() function to find the largest number
largest = max(list)

# Output the result
print("The maximum element in the list is:", largest)
```
### OUTPUT

```
The maximum element in the list is: 50
```
## 📋Problem 3: Count Occurrences of an Element in a List

**Question**: Write a program to count how many times a particular element occurs in a list.

**Solution**: [View Code](Problem3.py)

```python
# Define a list of numbers
list = [10, 20, 30, 20, 40, 20, 50]

# Define the element to count
element = 20

# Using built-in count() function
occurrences = list.count(element)

# Output the result
print(f"The element {element} occurs {occurrences} times in the list.")
```
### OUTPUT

```
The element 20 occurs 3 times in the list.
```
## 📋Problem 4: Remove Duplicates from a List

**Question**: Write a program to remove duplicate elements from a list.

**Solution**: [View Code](Problem4.py)

```python
# Define a list with duplicate elements
list = [10, 20, 30, 20, 40, 10, 50, 30]

# Remove duplicates while keeping order
unique_numbers = list(dict.fromkeys(list))

# Output the result
print("Original list:", list)
print("List after removing duplicates:", unique_numbers)
```
### OUTPUT

```
Original list: [10, 20, 30, 20, 40, 10, 50, 30]
List after removing duplicates: [10, 20, 30, 40, 50]
```
## 📋Problem 5: Sort a List of Numbers

**Question**: Write a program to take a list of numbers and print them in sorted order.

**Solution**: [View Code](Problem5.py)

```python
# Define a list of numbers
list = [10, 3, 45, 7, 23, 15]

# Sort the list in ascending order
sorted_numbers = sorted(list)

# Output the result
print("Original list:", list)
print("Sorted list:", sorted_numbers)
```
### OUTPUT

```
Original list: [10, 3, 45, 7, 23, 15]
Sorted list: [3, 7, 10, 15, 23, 45]
```
## 📋Problem 6: Merge Two Lists into One

**Question**: Write a program to merge two lists into a single list.
**Solution**: [View Code](Problem6.py)

```python
# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Merge lists using + operator
merged_list = list1 + list2

# Output the result
print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)
```
### OUTPUT

```
List 1: [1, 2, 3]
List 2: [4, 5, 6]
Merged List: [1, 2, 3, 4, 5, 6]
```