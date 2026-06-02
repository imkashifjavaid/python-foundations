'''
# * Continue Statement Work
employees  = ["Kashif", "Revealer", "Kash", "Revx"]
# want to search for: Revealer
#for, if, break
print(f"Finding RevealerX in List:  {employees} \n")
found = False
for employee in employees:
    if employee =="RevealerX":
        print(f"Employee Found: {employee}")
        found = True
        break
    print(f"Checking {employee} ...")

if found == False:
    print("Employee never found") 
'''

# * Continue Statement Work
employees = [
    "Ali", "", "Sara", "", "Ahmed", "Fatima", ""]

"""
#? Continue Problem Statement 1
Expected Output
Processing Employee: Ali
Processing Employee: Sara
Processing Employee: Ahmed
Processing Employee: Fatima
"""

#? Continue Problem Statement 1 Solution
for employee  in employees:
    if employee  == "":
        continue
    print(f"Processing Employee: {employee }")
