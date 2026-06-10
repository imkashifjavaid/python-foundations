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

with open("employees.txt", "r") as file:
    data = file.read()

print(data)