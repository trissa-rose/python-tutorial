n= int (input())
sum=0
for i in range (n):
    a = int (input())
    sum= a+sum
avg= (sum/n)
print("The average is: {:.2f}".format(avg))
    
#for getting 2 decimal places value use "{:._f}".format(). _mention the no. of decimal points.
#if round fn is used the 0 after the decimal is aborted causing error
