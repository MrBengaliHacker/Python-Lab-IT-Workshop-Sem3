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