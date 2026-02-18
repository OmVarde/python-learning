#you are given a list of programming language"
#["python", "java","C++","python","java","C"]
# Convert it into a set and print how many unique languages om knows
List = ["python", "java","C++","python","java","C"]
#how to convert list into set
om = set(List)
print(type(om))
print("Om know total numbers of",len(om),"languages.")