nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

squared_list = [[num**2 for num in sublist] for sublist in nested_list]

print("Squared Nested List:", squared_list)
