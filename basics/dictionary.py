"""Name: Kashif Javaid
Age: 27
Department: Game Development
Salary: 85000
Experience: 3
Is Active: True"""
#? Dictionary Dataset
employee = {"name": "Kashif Javaid", "age": 27, "department": "game development", "salary": 85000,
                    "experience" : 3, "is active" : True}

#? Task 1: Print Employee Name: Kashif Javaid
print(f"Employee Name: {employee["name"]}")

#? Task 2: Print Current Salary: 85000
print(f"Current Salary: {employee["salary"]}")

#? Task 3: Update Salary: 85000 -> 100000
employee["salary"] = 100000
print(f"Updated Salary: 85000 -> {employee['salary']}")

#? Task 4: Add New Field: location = Riyadh
employee["location"] = "Riyadh"
print(f"Employee Location: {employee["location"]}")