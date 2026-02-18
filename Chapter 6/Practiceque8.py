#Write a program to print numbers from 1 to 50 , but print "Om Varde"
# instead of numbers that are multiplies of 5 
# example output : 1 2 3 4 Om Varde  6 7 8 9 Om Varde.......

for item in range(1,50,1):
    if item%5 == 0:
        print("Om Varde")
    else:
        print(item)