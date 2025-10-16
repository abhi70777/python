paragraph = """Python is a powerful programming language that is easy to learn. 
This Python course is designed to help beginners understand the basics 
and build a strong foundation in programming."""

print(len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

preview = paragraph[:50]
print("\nPREVIEW 50 CHARACTERS:")
print(preview)

paragraph = paragraph.replace("Python", "PYTHON")
print("\nParagraph after replacement:")
print(paragraph)

print("\n PARAGRAPH IN LOWER CASE:")
print(paragraph.lower())

print("\n WHITESPACES REMOVED:")
print(paragraph.strip())


words = paragraph.split()
print("\n SPLIT METHOD :")
print(words)

if "course" in words:
    print("\nWORD COURSE:")
    print("\nThe word 'course' was found in the paragraph.")
else:
    print("\nThe word 'course' was NOT found in the paragraph.")

character = "183"
words = "26"
message = f"The course description is {character} characters long and has {words} words."
print("\n FINAL MESSAGE")
print(message)


