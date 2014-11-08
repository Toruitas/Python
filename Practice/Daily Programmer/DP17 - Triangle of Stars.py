__author__ = 'Stuart'
"""
write an application which will print a triangle of stars of user-specified height, with each line having twice as many stars as the last. sample output:
@
@@
@@@@
hint: in many languages, the "+" sign concatenates strings.
bonus features: print the triangle in reverse, print the triangle right justified
"""
def make_pyramid(height,upside_down = False):
    if upside_down == False:
        for i in range(height):
            print("@"*2**i)
    else:
        for i in range(height-1,-1,-1):
            print("@"*2**i)


def rjust_pyramid(height):
    max_width = 2**height
    for i in range(height):
        print(str.rjust("@"*2**i,max_width))

def another(height):
    s="@"
    for j in range(height):
        print(s)
        s+=s

def upsidedown(height):
    """
    the expression (x << y) means "Shift the binary representation of the integer x left by y places, then fill the space to the right with 0s." In arithmetic terms, this very efficiently implements the operation (x * 2y ). For example, 13 << 4 would be 0b1101 with four zeros on the right, so 0b11010000, which is 1324 = 1316=208.
    Since I have 1 << n, then I am doing 1*2n, so the integer the expression evaluates to is 2n. Therefore, s is a string of "@" symbols of length 2n.
    Since this is python and not C, I probably could have gotten away with 2**int(raw_input()) instead, but old habits die hard I guess.
    http://en.wikipedia.org/wiki/Logical_shift
    :param height:
    :return:
    """
    s="@"*(1 << height)
    while(s!="@"):
        s=s[:(len(s)/2)]
        print(s)

print(rjust_pyramid(4))
print(make_pyramid(4,True))
print(make_pyramid(4))