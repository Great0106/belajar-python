student = {
    "name": "Rauf Deriel",
    "class": "7th Grade",
    "address": "Serang, Banten"
}
print(student)

student["birthday"] = "1 Jun 2010"
student.pop("class")
print(student)

student.clear()
print(student)

del(student)
print(student)