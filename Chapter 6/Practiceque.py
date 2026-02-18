# Write a program to print the  multiplication table of any number 
# loop
# (hint : Start i=1 and run to the i <=10.)

n = int(input("Enter the number:"))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i +=1