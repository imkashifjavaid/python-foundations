#-------------------------------Self Assignment 1-------------------------------#
#---------------------------
#Section 1 - Player Information (variable practices and f-strings)
#---------------------------
#variables will be used in more than one sections for this assignment
player_name = "Kashif"
player_title = "Revealer"
player_class = "Knight" #Mage, warrior, Archer
player_level = 10
player_health = 100
player_stamina = 100
is_alive = True

player_username = "ksfrev"
player_password = "123"

#f-string
print("Section 1 output:")
print(f"{player_name} a.k.a {player_title} is on level {player_level} with {player_health} health")

#---------------------------
#Section 2 - Health Check System
#---------------------------
print("Section 2 output:")

if player_health <= 0:
    print(f"{player_name} died")
else:
    print(f"{player_name} is alive")
#---------------------------
#Section 3 - Level Rank System
#---------------------------
print("Section 3 output:")
if player_level >= 10:
    print(f"{player_name} is on Advanced Level")
elif player_level >= 5:
    print(f"{player_name} is on Medium Level")
else:
    print(f"{player_name} is on Beginner Level")
#---------------------------
#Section 4 - Player Class Checker
#---------------------------
print("Section 4 output:")

if  player_class == "Knight":
    print(f"Knight Class Detected")

elif player_class == "Archer":
    print(f"Archer Class Detected")

elif player_class == "Mage":
    print(f"Mage Class Detected")
else:
    print("Unknown class")
#---------------------------
#Section 5 - Comparison Operators along with f-strings
#---------------------------
print("Section 5 operators:")
numx1 = 5
numx2 = 10
print(f"Is {numx1} greater than {numx2}? {numx1 > numx2}")
print(f"Is {numx1} less than {numx2}? {numx1 < numx2}")
print(f"Is {numx1} equal to {numx2}? {numx1 == numx2}")
print(f"Is {numx1} not equal to {numx2}? {numx1 != numx2}")
print(f"Is {numx1} greater than or equal to {numx2}? {numx1 >= numx2}")
print(f"Is {numx1} less than or equal to {numx2}? {numx1 <= numx2}")

#---------------------------
#Section 6 - Login System Check
#---------------------------
print("Section 6 output:")
if player_username == "ksfrev" and player_password =="123":
    print("Login Successful")
else:
    print("Login Failed")

#---------------------------
#Section 7  - Type Check
#---------------------------
print("Section 7 output:")

print(type(player_class))
print(f"player_name has a value of {player_name} and has type of {type(player_name)}")

#---------------------------
#Section Bonus - Input from user
#---------------------------
print("Bonus Section output:")

player_username = input("Enter your username: ")

print(f"your username is {player_username}")

#---------------------------
#Section Mini Challlenge
#---------------------------
if player_stamina > 50 and player_health > 50:
    print(f"{player_name} is ready for battle")
else:
    print(f"{player_name} is weak for battle")