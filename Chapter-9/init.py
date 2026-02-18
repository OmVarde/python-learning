# __init__() is called automatically when a object is created
class student:
    institude = "ABC"

    def __init__(self,name,course):
        self.name = name
        self.course = course
om = student("Om","BE") #init method will be called
print("Student1:",om.name)
print("Course:",om.course)

