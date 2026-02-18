#Dictionary basics
Student = {
    "name": "Om Varde",
    "city": "Surat",
    "age": 25,
    "rollno.": 221120107064

}
print(Student["rollno."])
Student["name"] = "bhumi"
# to add any new key to dict
Student["behaviour"] = "attitude"
print(Student)
#remove a key from dict
Student.pop("behaviour")
print(type(Student))