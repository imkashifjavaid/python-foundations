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



#? Continue Problem Statement 1

# * Continue Statement Work
employees = [
    "Ali", "", "Sara", "", "Ahmed", "Fatima", ""]
"""
Expected Output
Processing Employee: Ali
Processing Employee: Sara
Processing Employee: Ahmed
Processing Employee: Fatima
"""

'''#? Continue Problem Statement 1 Solution
for employee  in employees:
    if employee  == "":
        continue
    print(f"Processing Employee: {employee }")
'''


'''
#? Continue Problem Statement 2
#? -1 means transaction failed
#? Expected Output
Processing transaction: 500
Processing transaction: 1200
Processing transaction: 300
Processing transaction: 750 
'''
#? Continue Problem Statement 2 Solution
transactions = [
    500,
    -1,
    1200,
    -1,
    300,
    750
]

for transaction  in transactions:
    if transaction  == -1:
        continue
    print(f"Processing transaction: {transaction }")