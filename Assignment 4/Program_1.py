# Create an empty dictionary
students = {}

# Take input for 5 students
for i in range(5):
    roll = int(input(f"Enter roll number of student {i+1}: "))
    name = input(f"Enter name of student {i+1}: ")
    students[roll] = name   # Add roll number as key and name as value

print("\nStudent Dictionary:")
print(students)