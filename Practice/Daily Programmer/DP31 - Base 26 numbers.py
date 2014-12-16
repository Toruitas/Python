__author__ = 'Stuart'
"""
Write a function that takes two base-26 numbers in which digits are represented by letters with A=0, B=1, … Z=25 and
returns their product using the same notation. As an example, CSGHJ × CBA = FNEUZJA.
Your task is to write the base-26 multiplication function.
Try to be very efficient in your code!
http://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/

SHIT how does base 26 work? Is CBA 2+1+0 or 0+(26+1)+(26+26+2)?
3B = 3×161+11×160 = 48+11 = 59
E7A9 = 14×163+7×162+10×161+9×160 = 57344+1792+160+9 = 59305
"""

base_god = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,
            "R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
god_base = {value:key for key,value in base_god.items()}

def from26(numerals):
    """
    Takes a numeral and turns it into a number
    :param numerals: CSGHJ
    :return: number value for assoc numeral
    """
    num = 0
    numeral_index = len(numerals)-1
    for i in range(len(numerals)):
        topup = base_god[numerals[i]]*26**numeral_index
        num += topup #base_god[numerals[i]]**numeral_index
        numeral_index -= 1
    return num

def from_dec(num):
    """
    divides by 26 a bunch, tallying the amount up. Then converts to letters
    :param num: number to convert to base26
    :return:base26number
    """
    base26 = ''
    while num > 0:
        rem = num % 26
        num = int(num/26)
        base26 += god_base[rem]
    return base26[::-1]

def multiply(string1,string2):
    return from_dec(from26(string1)*from26(string2))

if __name__ == "__main__":
    #print(multiply("CSGHJ","CBA"))
    print(from_dec(1234567))
    print(from26("CSGHJ"))