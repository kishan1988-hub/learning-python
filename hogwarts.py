# students = ["Hermonie","Harry","Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):  # combining range on list using len function
#     print(students[i])

# students = {
#             "Hermonie":"Gryffindor",
#             "Harry":"Gryffindor",
#             "Ron":"Gryffindor",
#             "Draco":"SLytherin"}  # dict usage
# for student in students:
#     print(student, students[student], sep=",")

students = [
    {"name":"Hermonie","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell Terrier"},
    {"name":"Draco","house":"Slytherin","patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=";")