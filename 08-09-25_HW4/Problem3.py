import random as rd

# Generate 5 random integers between 1 and 100
numbers = [rd.randint(1, 100) for _ in range(5)]
print("Generated numbers:", numbers)

# Calculate average
average = sum(numbers) / len(numbers)
print("Average:", average)
