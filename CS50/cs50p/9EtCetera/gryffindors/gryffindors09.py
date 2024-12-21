# enumerate
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])

# python gryffindors09.py
# 0 Hermione
# 1 Harry
# 2 Ron

# close but not quite right
for i in range(len(students)):
    print(i + 1, students[i])

# python gryffindors09.py
# 1 Hermione
# 2 Harry
# 3 Ron

# there's a better way