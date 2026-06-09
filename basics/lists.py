
#? List Data Set
employees = [
    "John Smith",
    "Emily Johnson",
    "Michael Brown",
    "Sophia Davis",
    "Daniel Wilson",
    "Olivia Taylor"
]

"""#* Step 1 — Printing total employees
print(len(employees))
print(f"Total number of employees: {len(employees)}")"""

"""#* Step 2 — Replace First Employee
#*Requirement: John Smith -> Kashif
print(f"Before Replacing Index 0: {employees}")
employees[0] = "Kashif"
print(f"After Replacing Index 0: {employees}")"""

"""#* Step 3 — Replace First Employee
employees.append("Emma Watson")
print(f"After appending: {employees}")"""

"""#* Step 4 — Remove Employee 4 "Daniel Wilson"
print(f"---Default List: {employees} ")
employees.pop(4) #? removing the entry using index [POP]
print(f"---Removed Daniel Wilson list: {employees} \n ")

#print(employees, "\n")
employees.remove("Michael Brown") #? removing the entry using value
print(f"---Removed Michael Brown list: {employees}")
"""

'''
"""#* Step 5 — Finding Index of employee at
print(f"List Display: {employees}")
x = employees.index("Olivia Taylor")
print(f"The Index value of {employees[5]} is {x}")"""

employees.insert(0, "Kashif Javaid")
print(employees)'''