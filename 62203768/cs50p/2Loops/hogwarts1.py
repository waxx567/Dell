# Introducing dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
# Whereas lists have locations that are numeric, dicts allow you to use words (keys)
# Print out values
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
print()
# Print out keys
for student in students:
    print(student)
print()
# Print out key:value pairs
for student in students:
    print(student, students[student], sep=", ")