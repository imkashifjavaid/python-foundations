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

"""Inventory_Items = ["Sword", "Shield", "Potions"]

for item in Inventory_Items:
    print("You have :", item) #Both have same outputs but in f string the FString joins first and then prints
    print(f"You have: {item}")"""

"""
#Question 1 : # Output Weapon Equipped: Sword
Weapon_List = ["Sword", "Axe", "Bow" ,"Dagger"]

for weapon in Weapon_List:
    print(f"Weapon Equipped {weapon}")
"""


"""
#Question 2 : # Outputs Expected
Party Member 1: Kashif
Party Member 2: Ali
Party Member 3: Sara
Party Member 4: Ahmed
"""

Party_Member_Names = ["Ali", "Sara", "Ahmed"]
count = 1

for members in Party_Member_Names:
    print(f"Party Member {count} : {members}")
    count = count + 1