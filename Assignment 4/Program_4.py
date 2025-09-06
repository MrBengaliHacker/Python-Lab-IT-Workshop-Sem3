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

# Print the merged dictionary
print("Merged dictionary:", merged_dict)