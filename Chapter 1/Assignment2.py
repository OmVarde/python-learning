# take diameter as an input and calculate the area of the circle
d=int(input('enter the diameter to find the area of circle:'))
# isko int mein wrap krdiya kyuki str ko divide nai kr skte
r=d/2
a=3.14* (r ** 2)/4
print ('Radius of the circle is:',r)
print ('Area of circle is:',a)