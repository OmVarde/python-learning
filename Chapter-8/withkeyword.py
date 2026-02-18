#with keyword is use because it automatically close the file
# try and except is use to avoid any crash

with open("Chapter-8/report.txt","r") as f:
    data = f.read()
    print(data) 

# To read line by line 
try:
    with open("Chapter-8/report.txt","r") as f:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readlines()
        print(line1)
        print(line2)
        print(line3)
except:
    print("Does not have that file")
# read everylines 
with open("Chapter-8/report.txt","r") as f:
    data = f.readlines()
    print(data) 