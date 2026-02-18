# write a python program that takes  number as input and prints:
# "positive" if no.  > 0
# "zero" if no. == 0
# "negative" if no. < 0
digit = int(input("Enter a number:"))
if digit > 0:
    print("Positive")
elif digit < 0:
    print("Negative")
else:
    print("Zero")