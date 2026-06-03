"""Name: Kashif Javaid
Age: 27
Department: Game Development
Salary: 85000
Experience: 3
Is Active: True"""
#? Dictionary Dataset
employee = {"name": "Kashif Javaid", "age": 27, "department": "Game Development", "salary": 85000,
                    "experience" : 3, "is_active" : True}

#? Task 1: Print Employee Name: Kashif Javaid
print(f"Employee Name: {employee['name']}")

#? Task 2: Print Current Salary: 85000
print(f"Current Salary: {employee['salary']}")

#? Task 3: Update Salary: 85000 -> 100000
employee['salary'] = 100000
print(f"Updated Salary: 85000 -> {employee['salary']}")

#? Task 4: Add New Field: location = Riyadh
employee['location'] = "Riyadh"
print(f"Employee Location: {employee['location']}")

#? Task 5: Print Complete Dictionary
print(f"Full Dictionary: {employee}")

#? Bonus Task: Print Total Employee Fields
print(f"Total Fields of Dictionary: {len(employee)}")