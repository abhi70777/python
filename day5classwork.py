python = {"Abhi","Hari","Ragnor"}

Data_Science = {"Abin","Issac","Ragnor"}

python.add("Ben")
print("ADD:", python)


Data_Science.remove("Abin")
print("REMOVE:", Data_Science)

both_courses = python & Data_Science
print("Students in both courses:", both_courses)

print( "ONLY;", python-Data_Science)

print("ALL;", python|Data_Science)

course_dict = {
    "Python": len(python),
    "Data Science": len(Data_Science)
}

print("dict;", course_dict)

for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_dict.items()}
print("Expected growth:", expected_growth)






