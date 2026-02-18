#print a multiplication table of any number using a loop
numbercount = int(input("Enter the number:"))
for item in range(1,11,1):
    print(f"{numbercount} * {item} = {numbercount*item}")
