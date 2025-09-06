# Dictionary of employees
employees = {
    101: {"name": "Ritam", "department": "CSE", "salary": 60000},
    102: {"name": "Rupkatha", "department": "CSE", "salary": 60000},
    103: {"name": "Amit", "department": "ECE", "salary": 50000},
    104: {"name": "Neha", "department": "ME", "salary": 48000},
    105: {"name": "Mr. Bengali Hacker", "department": "Unknown", "salary": 100000}
}

# Function to print employees of a specific department
def employees_in_department(dept_name):
    print(f"Employees in {dept_name} department:")
    found = False
    for emp_id, details in employees.items():
        if details["department"].upper() == dept_name.upper():
            print(f"ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}")
            found = True
    if not found:
        print("No employees found in this department.")

# Function to find employee with maximum salary
def max_salary_employee():
    max_salary = -1
    emp_with_max_salary = None
    for emp_id, details in employees.items():
        if details["salary"] > max_salary:
            max_salary = details["salary"]
            emp_with_max_salary = (emp_id, details)
    emp_id, details = emp_with_max_salary
    print(f"\nEmployee with maximum salary:")
    print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Salary: {details['salary']}")

# Demo
employees_in_department("CSE")
max_salary_employee()