"""Today we will be making some simple 8x8 bitmap pictures. You will be given 8 hex values that can be 0-255
in decimal value (so 1 byte). Each value represents a row. So 8 rows of 8 bits so a 8x8 bitmap picture.

8 Hex values.
example:
18 3C 7E 7E 18 18 18 18

A 8x8 picture that represents the values you read in.
For example say you got the hex value FF. This is 1111 1111 . "1" means the bitmap at that location is on and print something. "0" means nothing is printed so put a space. 1111 1111 would output this row:
xxxxxxxx
if the next hex value is 81 it would be 1000 0001 in binary and so the 2nd row would output (with the first row)
xxxxxxxx
x      x

   xx
  xxxx
 xxxxxx
 xxxxxx
   xx
   xx
   xx
   xx

FF 81 BD A5 A5 BD 81 FF
AA 55 AA 55 AA 55 AA 55
3E 7F FC F8 F8 FC 7F 3E
93 93 93 F3 F3 93 93 93
"""


def hex_to_binary(hexstring):
    for hexes in hexstring:
        binary_strings.append(bin(int('1'+hexes, 16))[3:])
        """adds leading 1 to string so any leading 0's aren't dropped
         in conversion to int. bin converts to binary, 16 is the scale equivalent to binary, then [3:] slices
         the leading 1 off again"""
    return binary_strings

def printout(binarystring):
    for binary in binarystring:
        print(binary.replace("1","X").replace("0"," ")) #replace both 1's and 0's


#if __name__ == "__main__":
    #hex_strings = ["FF", "81", "BD", "A5", "A5", "BD", "81", "FF"]
    #binary_strings = hex_to_binary(hex_strings)
    #printout(binary_strings)

if __name__== "__main__": #Consolidating
    for hexes in ["93", "93", "93", "F3", "F3", "93", "93", "93"]:
        print((bin(int('1'+hexes,16))[3:]).replace("1","X").replace("0"," "))

