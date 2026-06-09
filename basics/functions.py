"""def greet(): # function definition
    print("Good Noon Kashif")
    
greet() #function calls
"""


"""task 1
def my_intro():
    print("My name is Kashif")
    print("Im learning python")
    print("Im currently living in KSA")        
my_intro()
"""
#task 2
"""
def sum_2(a, b):
   # return num1 + num2
    print(f"Sum: {a+b}")
sum_2(2,2)
"""
#task 2 with return saved
'''def sumx(a,b,c):
    res = a + b + c 
    print(f"Sum: {res}")
    return 
    
sumx(2,2,2)
'''



'''def show_employee(Name, Dep):
    print(f"Employee Name: {Name}")
    print(f"Department: {Dep}")

show_employee("Kashif Javaid", "Game Dev")
'''

'''#? Task 1 - Multiply Numbers

def prod(a,b):
    result = a * b
    print(f"Product ={result}" )
    return result

prod(2,2)'''

'''
#? print Task 2 - Full Name

def f_name(a,b):
    result = a + " " + b
    print(f"Full Name:  {result}")
    return 

f_name("Kashif", "Javaid")

'''

'''#Dry Running Code
def multiply(a, b): #3,4
    result = a * b #12
    print(result)  #printed 12
    return result #saved result 12

x = multiply(3, 4) #12 used above

print(x) # 12 will be printed 

#final output: 12
#            : 12'''


# calc areq

'''def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 4)
area2 = calculate_area(10, 8)

print("Area 1:", area1)
print("Area 2:", area2)

'''

#? Task 1: Create Function employee_salary(name, salary)
#? Expected Output:
# Employee: Emma Wilson
# Salary: 92000

'''def employee_salary(name,salary):
    print(f"Employee: {name} \nSalary: {salary}")

#    return name
employee_salary("Emma Wilson", 92000)
'''



"""
#? Task 2: Create Function annual_salary(monthly_salary)

Requirement:
- Function should accept monthly_salary
- Return yearly salary
- Use return, not print

Expected:

result = annual_salary(5000)

print(result)

Output:
60000
"""

'''monthly_salary = int(input("Enter your monthly salary: "))
#a = 12
def yearly_salary(monthly_salary):
    result = monthly_salary * 12
    return result

annual_salary = yearly_salary(monthly_salary)

print(f"Annual Salary: {annual_salary}")'''




"""
A company stores whether an employee is currently working in the organization or not.
Create a function named employee_status that accepts a single parameter called is_active.
If the employee is active, the function should display a message indicating that the employee is currently working in the company.
If the employee is not active, the function should display a message indicating that the employee is no longer working in the company.
Test your function with both active and inactive employees.
"""


#employee_is_active = False

'''def employee_status(employee_is_active):
    if employee_is_active:
        print("Employee is currently working in the company")
    else:
        print("Employee isn't currently working in the company")


employee_status(False)

'''

"""
Create a function that accepts a complete employee dictionary
and prints the employee's name and salary.E

Example:

employee = {
    "employee_name": "Emma Wilson",
    "salary": 92000
}

show_employee(employee)
"""

'''employee = {
    "employee_name": "Emma Wilson",
    "salary": 92000
}

def show_employee(employee):
    print(f"Employee Name: {employee['employee_name']}")
    print(f"Employee salary: {employee['salary']}")
   # print(f"Employee Salary{1}")

show_employee(employee)'''


"""

'''#? Task 5: Create Function show_all_employees(employees)

Requirement:
- Accept a list of employee dictionaries
- Loop through all employees
- Print employee names

Expected Output:
Kashif Javaid
Revealer
Kashx
"""
'''
employee1 = {"employee_name" : 'Kashif Javaid' , "age" : 29 }
employee2 = {"employee_name" : 'Revealer' , "age" : 35}
employee3 = {"employee_name" : 'Kashx' , "age" : 28}

employee_list = [employee1, employee2, employee3 ]

def show_all_employees(employee_list):
    for employee in employee_list:
        print(employee['employee_name'])

show_all_employees(employee_list)
'''




"""
A company's HR department maintains a list of employee records.
The HR manager wants a feature that can search for a specific employee by name.
Create a function named find_employee that accepts:
1. A list of employee dictionaries



2. The name of the employee to search for
The function should check every employee record in the list.
If the employee exists in the records, display:
Employee Found
If the employee does not exist in the records, display:
Employee Not Found
Test your function with:
"Revealer"
and
"Ali Khan"
One should be found and the other should not be found.
"""

employee_1 = {"name": 'Kashif', "age" : 29 , "location" : 'Riyadh' }
employee_2 = {"name": 'Rev', "age" : 25 , "location" : 'KSA' }
employee_3 = {"name": 'Revealer', "age" : 0 , "location" : 'World' }
employee_db = [employee_1, employee_2, employee_3]

def find_employee(employee_db): #?  contains all list of employee dictionaries
    for employee in employee_db:  #? employee contains all 3 elements of list
        if employee["name"] == 'Rev':  #? employee name is on index [0] of each dictionary used comparison operator
            print("Employee Found") #? If found print then break else show not found
            break
        else:
            print("Employee not found")

find_employee("Rev") #called func()

