#try to add both integer 9 and float 9.0 to a set and observe what happens

setA = set()
print(type(setA))
x = 9
y = str(9.0)

setA.add(x)
setA.add(y)
print(setA)