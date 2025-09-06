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