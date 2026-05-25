
#---------------------------
#Section 1 - Player Information (variable practices and f-strings)
#---------------------------
#variables will be used in more than one sections for this assignment
player_name = "Kashif"
player_title = "Revealer"
player_level = 10
player_health = 100
player_stamina = 100
is_alive = True
#f-string
print("Section 1 output:")
print(f"{player_name} a.k.a {player_title} is on level {player_level} with {player_health} health")

#---------------------------
#Section 2 - Health Check System
#---------------------------
print("Section 2 output:")

if(player_health <= 0):
    print(f"{player_name} died")
else:
    print(f"{player_name} is alive")
#---------------------------
#Section 3 - Level Rank System
#---------------------------
print("Section 3 output:")
if(player_level >= 10):
    print(f"{player_name} is on Advance Level")
elif(player_level >= 5):
    print(f"{player_name}  is on Medium Level")
else:
    print(f"{player_name}  is on Beginner Level")
