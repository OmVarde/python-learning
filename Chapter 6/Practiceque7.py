# write a program using for and range() to print all even numbers between 
# 1 and 20 

for item in range(1,20):
    if item%2 == 0 :
        print(item)
    
# there is one more method to do it 

for item in range(2,21,2):
    print(item)