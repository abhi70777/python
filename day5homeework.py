Frontend_course = {"Abhi","Hari","Ragnor"}

Backend_course = {"Abin","Issac","Ragnor"}

Backend_course.add("Ben")
print("ADD;",Backend_course)

Frontend_course.remove("Abhi")
print("REMOVE;", Frontend_course)

both_courses = Frontend_course & Backend_course
print("Students in both courses:", both_courses)

print("ONLY:", Backend_course-Frontend_course)

print("UNIQUE;", Frontend_course|Backend_course)

course_enrollments = {
    "Frontend": len(Frontend_course),
    "Backend": len(Backend_course)
}

print("DICT:",course_enrollments)

for course, count in course_enrollments.items():
    print(f"Course: {course}, Students: {count}")

extended_courses = {
    **course_enrollments,
    "Fullstack": len(Frontend_course| Backend_course)
}
print("Extended course enrollments:", extended_courses)