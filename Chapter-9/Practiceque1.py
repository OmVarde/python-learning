# Create a class Student that takes 3 marks and has a method average()
class Student:
    def __init__(self,name,listofmarks):
        self.name = name
        self.listofmarks = listofmarks

    def average(self):
        sum = 0
        for eachvalue in self.listofmarks:
            sum = eachvalue+sum
            avg = sum/3
        print(self.name)
        print("Average is:",avg)
        

s1  = Student("Om",[99,89,78])
s1.average()
