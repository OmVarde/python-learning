# Print a countdown before something "exciting" happens 
# concept used: for loop , range()  , the time module
import time

timer = int(input("Enter the Number:"))
for item in range(timer,0,-1):
    print(item)
    time.sleep(1)
print("WOOHHOOO! Happy New Year")