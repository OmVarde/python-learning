# create a console  based Expense tracker program in tracker in python
# all task must be implemented using loops, if-else, lists, and dictionaries
# Expense Tracker Project

expenses = [] # all the expenses of user in form of dictionary
print("Welcome to the Expense Tracker")

while True:
    print("==== MENU ====")
    print("1. Add your Expense")
    print("2. View Expense")
    print("3. View total Money spent")
    print("4. Exit")

    choice = int(input("Enter your Choice:"))
# 1.add expense
    if choice == 1:
        Date = input("Enter the date:")
        Category = input("Enter the category:")
        Description = input("Enter more detail about expense:")
        Amount = float(input("Enter the amount:"))

        Expense = {
            "Date": Date,
            "Category": Category,
            "Description": Description,
            "Amount": Amount
            
        }
        expenses.append(Expense)
        print( "\nDONE bro expense is added succesfully")
# 2.view expense
    elif choice == 2:
        if len(expenses) == 0:
            print("No Expense Added")
        else:
            print("==== Here is your all expense ====")
            count = 1
            for everyspent in expenses:
                print(f"Expense {count}--> {everyspent["Date"]}, {everyspent["Category"]}, {everyspent["Description"]}, {everyspent["Amount"]} ")
                count += 1
# 3. View total money spent
    elif choice == 3:
        if len(expenses) == 0:
            print("No Amount Spent")
        else:
            total = 0
            for spent in expenses:
                total = total + spent["Amount"]
            print("Your total Amount is",total)    
# 4. exit
    elif choice == 4:
        print("Thanks for using our Program, Visit Again")
        break

    else:
        print("please enter valid choice, try again")
