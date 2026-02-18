# write code to open a file named mydata.txt in read mode
file = open("Chapter-8/mydata.txt","r")
data = file.read()
print(data)
file.close()