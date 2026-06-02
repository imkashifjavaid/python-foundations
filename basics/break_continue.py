employees  = ["Kashif", "Revealer", "Kash" "Revx"]
# want to search for: Revealer
#for, if, break

for employee in employees:
    if employee =="Revealer":
        print(f"Employee Found: {employee}")
        break
    else:
        print(f"Checking {employee} ...")

