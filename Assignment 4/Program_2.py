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