
employee1 = {"employee_name": 'Emma Wilson',
    "age" : 31,
    "department" : 'Human Resources',
    "salary": 92000,
    "experience" : 7,
    "location" : 'London',
    "is_active" : True
    }

employee2 = {
    "employee_name": 'Ryan Cooper',
    "age" : 29,
    "department" : 'Software Engineering',
    "salary": 105000,
    "experience" : 5,
    "location" : 'Toronto',
    "is_active" : True
    }

employee3 = {
    "employee_name": 'Sophia Davis',
    "age": 35,
    "department": 'Finance',
    "salary": 115000,
    "experience": 10,
    "location": 'New York',
    "is_active": False
}
all_employees = [employee1, employee2, employee3]
# print(all_employees)
#? Task 1: Print all employee names using loop
'''
for employee in all_employees:
    print(f"employee name: {employee['employee_name']}")
'''

'''#? Task 2: Print all employee names using loop, enumerate
for count, employee in enumerate(all_employees, start= 1):
    print(f"Employee {count} {employee['employee_name']}")'''

'''    #? Task 3: Print all employee salaries
for employee in all_employees:
    print(employee['salary'])
'''

'''    #? Task 3: Print all employee salaries using enumerate
for index, employee in enumerate(all_employees,start= 1):
        print(index ,employee['salary'] )
'''

#? Task 4: Print employee name, salary and location
for employee in all_employees:
    print(f"Employee Name: {employee['employee_name']} \nSalary:{employee['salary']} \nLocation: {employee['location']}\n")