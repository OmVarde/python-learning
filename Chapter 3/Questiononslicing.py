#take input and print middle 3 characters and last 2 chars
str= input("Enter a value:" )
mid = len(str)//2
output1 = str[mid -1:mid+2]
print(output1)
last = str[-2:]
print(last)