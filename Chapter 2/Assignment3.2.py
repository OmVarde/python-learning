# write a program that takes the total bill amount and number of friends as input calculate 
# how much each person will pay

total = float(input("Enter the total amount of expense:"))
Person = int(input("Enter the total person:"))
split = total / Person
print ("The split for each person is", split)