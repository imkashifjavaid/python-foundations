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




#print("Employee not found")

