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
