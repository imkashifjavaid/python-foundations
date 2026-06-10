with open("employees.txt", "w") as file:
    file.write("Kashif Javaid")



with open("employees.txt", "w") as file:
    file.write("Kashif Javaid")
    
    
"""
#? Task 2
Read employees.txt
Print its contents on screen
Expected Output:
Kashif Javaid
"""

"""
with open("employees.txt", "r") as file:
    data = file.read()

print(data)
"""

"""
#? Task 3

Requirement:
- Open employees.txt in append mode
- Add a new employee named "Revealer"
- Read the file again
- Print complete file contents

Expected Output:

Kashif Javaid
Revealer
"""

with open("employees.txt", "a") as file:
    file.write("\nRevealer")

with open("employees.txt", "r") as file:
    data = file.read()

print(data)
