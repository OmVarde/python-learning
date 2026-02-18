# print how many lines are present in certificate.txt
with open("Chapter-8/certificate.txt","r") as f:
    data = f.readlines()
    print(len(data))