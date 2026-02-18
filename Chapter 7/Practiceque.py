# write a function show_age(name,age) that prints:
# Om is 22 years old.

def show_age(name,age):
    print(f"{name} is {age} years old.")

show_age("Om",22)

# default value assingning to avoid any error is no value is passed
def name_age(name="Om", age=22):
    print(f"My name is {name} and my age is {age}.")

name_age()
name_age("Mohan",43)