list = [1, 2, 3, 4, 5, 6, 7, 8]

# Generate squares of even numbers only
squares = [x ** 2 for x in list if x % 2 == 0 ]

print("The squares of even numbers =",squares)