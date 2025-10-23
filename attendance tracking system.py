attendance = [18, 20, 19, 15, 21]

full_days = 0

for students in attendance:
    if students >=20:
       print("full")
       full_days += 1
else:
    print("Not Full")

total_attendance= sum(attendance)

print("Number of Full_day:" , full_days)

print("total_attendance:", total_attendance)