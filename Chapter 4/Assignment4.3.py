#Write a program to check grade based on marks(A/B/C/D)
grades = int(input("Enter your grade:"))
if grades >= 90:
    print("Your Grade is A")
elif grades >= 80:
    print("Your Grade is B")
elif grades >= 70:
    print("Your Grade is C")
else:
    print("Your Grade is D")