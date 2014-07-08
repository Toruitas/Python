x, y, z = 2, 4, 0

if ((x%2!=0)  or (y%2!=0) or (z%2!=0)):
    if(x%2!=0):
        if(y%2!=0 and y>x and y>z):
            print str(y)
        elif(z%2!=0 and z>x and z>y):
            print str(z)
        else:
            print str(x)
    elif(y%2!=0):
        if(x%2!=0 and x>y and x>z):
            print str(x)
        elif(z%2!=0 and z>x and z>y):
            print str(y)
        else:
            print str(y)
    else:
        print str(z)
else:
    print "There are no odds!"
    