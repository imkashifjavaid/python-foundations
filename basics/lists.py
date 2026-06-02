
#? List Data Set
employees = [
    "John Smith",
    "Emily Johnson",
    "Michael Brown",
    "Sophia Davis",
    "Daniel Wilson",
    "Olivia Taylor"
]

#* Step 1 — Printing total employees
print(len(employees))
print(f"Total number of employees: {len(employees)}")

#* Step 2 — Replace First Employee
#*Requirement: John Smith -> Kashif
print(f"Before Replacing Index 0: {employees}")
employees[0] = "Kashif"
print(f"After Replacing Index 0: {employees}")
