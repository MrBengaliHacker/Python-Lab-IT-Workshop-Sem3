my_tuple = (10, 20, 30, 40, 50)
temp_list = list(my_tuple)

temp_list[2] = 69  # replacing element at index 2
new_tuple = tuple(temp_list)

print("Modified Tuple:", new_tuple)
