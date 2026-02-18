# take input in celsius and print its equivalent in the fahrenheit and kelvin
C = int(input("Enter the value of temperature in celsius:"))
f = C * (9/5) + 32
k = C + 273.15
print("The temperature in Fahrenheit is:", f)
print("The temperature in Kelvin is:", k)