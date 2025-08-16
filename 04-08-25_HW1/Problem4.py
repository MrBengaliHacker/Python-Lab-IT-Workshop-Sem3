# Define a list with duplicate elements
list = [10, 20, 30, 20, 40, 10, 50, 30]

# Remove duplicates while keeping order
unique_numbers = list(dict.fromkeys(list))

# Output the result
print("Original list:", list)
print("List after removing duplicates:", unique_numbers)
