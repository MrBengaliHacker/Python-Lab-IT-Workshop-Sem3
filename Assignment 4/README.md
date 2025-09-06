## 📋Program 1: Student Dictionary

**Question**: Write a Python program to create a dictionary of 5 students with their roll numbers as keys and names as values. Print the dictionary.

**Solution**: [View Code](Program_1.py)

```python
# Create an empty dictionary
students = {}

# Take input for 5 students
for i in range(5):
    roll = int(input(f"Enter roll number of student {i+1}: "))
    name = input(f"Enter name of student {i+1}: ")
    students[roll] = name   # Add roll number as key and name as value

print("\nStudent Dictionary:")
print(students)
```
### OUTPUT

```
Enter roll number of student 1: 101
Enter name of student 1: Ram
Enter roll number of student 2: 102
Enter name of student 2: Shyam
Enter roll number of student 3: 103
Enter name of student 3: Jodu
Enter roll number of student 4: 104
Enter name of student 4: Modhu
Enter roll number of student 5: 105
Enter name of student 5: Kodu

Student Dictionary:
{101: 'Ram', 102: 'Shyam', 103: 'Jodu', 104: 'Modhu', 105: 'Kodu'}
```
## 📋Program 2: Fruit Price Dictionary

**Question**: Create a dictionary of fruits with their prices. Ask the user to input a fruit name and print its price. If the fruit is not available, display "Not Found".

**Solution**: [View Code](Program_2.py)

```python
# Dictionary of fruits with prices
fruits = {
    "mango": 90,
    "banana": 40,
    "apple": 120,
    "grapes": 70,
    "pineapple": 150
}

fruit_name = input("Enter the fruit name: ").lower()

# Check availability
if fruit_name in fruits:
    print(f"The price of {fruit_name} is: {fruits[fruit_name]}")
else:
    print("Not Found")
```
### OUTPUT

```
Enter the fruit name: Pineapple
The price of pineapple is: 150
```
```
Enter the fruit name: Berry
Not Found
```
## 📋Program 3: Add and Update Dictionary

**Question**: Write a program to add a new key–value pair in a dictionary and update the value of an existing key.

**Solution**: [View Code](Program_3.py)

```python
# Sample dictionary
my_dict = {
    "name": "Ritam",
    "age": 19,
    "branch": "CSE"
}

# Print original dictionary
print("Original dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Adding a new key-value pair
my_dict["college"] = "Bengal Institute of Technology"

# Updating the value of an existing key
my_dict["age"] = 20

# Print updated dictionary
print("\nUpdated dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
### OUTPUT

```
Original dictionary:
name: Ritam
age: 19
branch: CSE

Updated dictionary:
name: Ritam
age: 20
branch: CSE
college: Bengal Institute of Technology
```
## 📋Program 4: Merge Two Dictionaries with Summed Values

**Question**: Write a program to merge two dictionaries into one. If a key is present in both, sum their values.

Example:

d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
Output → {'a': 10, 'b': 50, 'c': 40}

**Solution**: [View Code](Program_4.py)

```python
# Two dictionaries
d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}

# Merging dictionaries
merged_dict = d1.copy()  # Start with d1

for key, value in d2.items():
    if key in merged_dict:
        merged_dict[key] += value  # Sum values if key exists
    else:
        merged_dict[key] = value   # Add new key-value pair

print("Merged dictionary:", merged_dict)
```
### OUTPUT

```
Merged dictionary: {'a': 10, 'b': 50, 'c': 40}
```
## 📋Program 5: Sort Dictionary by Keys and Values

**Question**: Create a dictionary of items and their prices. Sort the dictionary by:

Keys (alphabetical order)

Values (ascending order of prices)

**Solution**: [View Code](Program_5.py)

```python
# Dictionary of items with prices
shop_items = {
    "chocolate": 25,
    "milk": 50,
    "bread": 30,
    "butter": 80,
    "eggs": 60
}

# Print original dictionary
print("Original Dictionary :", shop_items)

# Sort dictionary by keys (alphabetical order)
sorted_by_keys = dict(sorted(shop_items.items()))
print("\nSorted By Keys :", sorted_by_keys)

# Sort dictionary by values (ascending order)
sorted_by_values = dict(sorted(shop_items.items(), key=lambda item: item[1]))
print("\nSorted By Values:", sorted_by_values)
```
### OUTPUT

```
Original Dictionary : {'chocolate': 25, 'milk': 50, 'bread': 30, 'butter': 80, 'eggs': 60}

Sorted By Keys : {'bread': 30, 'butter': 80, 'chocolate': 25, 'eggs': 60, 'milk': 50}

Sorted By Values: {'chocolate': 25, 'bread': 30, 'milk': 50, 'eggs': 60, 'butter': 80}   
```
## 📋Program 6: Menu-Driven Book Management System

**Question**: Create a dictionary where keys are book IDs and values are book names. Implement functions for:

Adding a new book

Removing a book

Searching for a book by ID

Displaying all books

**Solution**: [View Code](Program_6.py)

```python
# Dictionary to store books
books = {}

# Function to add a new book
def add_book():
    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    if book_id in books:
        print(f"Book ID {book_id} already exists with name '{books[book_id]}'.")
    else:
        books[book_id] = book_name
        print(f"Book '{book_name}' added with ID {book_id}.")

# Function to remove a book
def remove_book():
    book_id = int(input("Enter Book ID to remove: "))
    if book_id in books:
        removed = books.pop(book_id)
        print(f"Book '{removed}' with ID {book_id} removed.")
    else:
        print(f"No book found with ID {book_id}.")

# Function to search for a book by ID
def search_book():
    book_id = int(input("Enter Book ID to search: "))
    if book_id in books:
        print(f"Book found: ID {book_id} → '{books[book_id]}'")
    else:
        print(f"No book found with ID {book_id}.")

# Function to display all books
def display_books():
    if books:
        print("All books in the library:")
        for book_id, book_name in books.items():
            print(f"ID {book_id} → {book_name}")
    else:
        print("No books available.")

# Menu-driven system
while True:
    print("\n=== Book Management System ===")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search a Book by ID")
    print("4. Display All Books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
```
### OUTPUT

```
=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 1
Enter Book ID: 101
Enter Book Name: Python Basics
Book 'Python Basics' added with ID 101.

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 1
Enter Book ID: 102
Enter Book Name: Data Structures
Book 'Data Structures' added with ID 102.

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 4
All books in the library:
ID 101 → Python Basics
ID 102 → Data Structures

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 3
Enter Book ID to search: 101
Book found: ID 101 → 'Python Basics'

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 2
Enter Book ID to remove: 102
Book 'Data Structures' with ID 102 removed.

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 4
All books in the library:
ID 101 → Python Basics

=== Book Management System ===
1. Add a Book
2. Remove a Book
3. Search a Book by ID
4. Display All Books
5. Exit
Enter your choice (1-5): 5
Exiting the system. Goodbye!
```
## 📋Program 7: Employee Dictionary – Department & Maximum Salary

**Question**: Create a dictionary of employees where key = employee ID and value = another dictionary containing (name, department, salary).

Print employees of a specific department.

Find the employee with the maximum salary.

**Solution**: [View Code](Program_7.py)

```python
# Dictionary of employees
employees = {
    101: {"name": "Ritam", "department": "CSE", "salary": 60000},
    102: {"name": "Rupkatha", "department": "CSE", "salary": 60000},
    103: {"name": "Amit", "department": "ECE", "salary": 50000},
    104: {"name": "Neha", "department": "ME", "salary": 48000},
    105: {"name": "Mr. Bengali Hacker", "department": "Unknown", "salary": 100000}
}

# Function to print employees of a specific department
def employees_in_department(dept_name):
    print(f"Employees in {dept_name} department:")
    found = False
    for emp_id, details in employees.items():
        if details["department"].upper() == dept_name.upper():
            print(f"ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}")
            found = True
    if not found:
        print("No employees found in this department.")

# Function to find employee with maximum salary
def max_salary_employee():
    max_salary = -1
    emp_with_max_salary = None
    for emp_id, details in employees.items():
        if details["salary"] > max_salary:
            max_salary = details["salary"]
            emp_with_max_salary = (emp_id, details)
    emp_id, details = emp_with_max_salary
    print(f"\nEmployee with maximum salary:")
    print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Salary: {details['salary']}")

# Demo
employees_in_department("CSE")
max_salary_employee()
```
### OUTPUT

```
Employees in CSE department:
ID: 101, Name: Ritam, Salary: 60000
ID: 102, Name: Rupkatha, Salary: 60000

Employee with maximum salary:
ID: 105, Name: Mr. Bengali Hacker, Department: Unknown, Salary: 100000
```