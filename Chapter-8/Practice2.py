# write the program to read a text from a given file certificate.txt 
#and find whelther it contains the word live
file = open("Chapter-8/certificate.txt")
data = file.read()
data = data.lower()
if "live" in data:
    print("Yes there is word live")
else:
    print("Nope its not")
file.close()