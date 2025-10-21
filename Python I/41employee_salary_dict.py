# Write a program to create a dictionary by combining two lists 'name' for employee name and 'salary' for employee salary. Use the list 'name' as the key and ‘salary’ as the value of dictionary elements.

num_employees = int(input("Enter the number of employees: "))

names = []
salaries = []
employee_data = {}

for i in range(num_employees):
    names.append(input("Enter Name: "))
    salaries.append(int(input("Enter Salary: ")))
    employee_data[names[i]] = salaries[i]

print("Created Dictionary:", employee_data)
