# what if we wanted not a list of dictionaries but one big dict with all the info therein
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

# python gryffindors07.py
# {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}