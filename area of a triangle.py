import math
a = float (input ())
b = float (input ())
c = float (input ())
if a+b>=c and a+c>=b and b+c>=a and a>0 and b>0 and c>0:
    s = ((a+b+c)/2)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print ("The area of the triangle is: {:.2f}".format(area))
else:
    print ("Invalid Triangle")
    
