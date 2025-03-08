n= int (input())
A=0
i=0
for i in range (n):
    a = int (input())
    A= a+A
    avg= (A/n)
print("The average is: {:.2f}".format(avg))
    
#for getting 2 decimal places value use "{:._f}".format(). _mention the no. of decimal points.
