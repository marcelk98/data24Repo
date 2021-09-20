student = {
    "name":"marcel",
    "stream":"data",
    "lessons": ["data types","variables","SQL"]
}

student["lessons"].remove("variables")

print([student["lessons"]])

print(student.keys())
print(student.values())