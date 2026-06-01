# For Loops

#Printing list using for loops
''' Names = ["Sara", "Ali", "Usman", "Areeba","Hassan"]
for name in Names:
    print(name) '''

#using range function
"""for i in range(2,10):
    print(i)"""

"""for i in range(2,12,2): #start, stop before, jump of
    print(i)"""

"""for i in range(15):
    print("HBD Kashif")
"""

Inventory_Items = ["Sword", "Shield", "Potions"]

for item in Inventory_Items:
    print("You have :", item) #Both have same outputs but in f string the FString joins first and then prints
    print(f"You have: {item}")