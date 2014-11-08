__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/
You're challenge for today is to create a program that can calculate pi accurately to at least 30 decimal places.
Try not to cheat :)

look up theory of how to find pi, then use bisection search?
area = pi * r **2
pi = area / (r**2)
http://www.wikihow.com/Calculate-Pi Nilakantha series
http://en.wikipedia.org/wiki/Pi#Computer_era_and_iterative_algorithms
"""

def findpi(radius, area):
    return area/(radius**2)

def findpi_infseries():
    """
    Uses Nilakantha series to find Pi
    :return: Pi to 30 digits
    """
    from decimal import getcontext
    digits = 30
    getcontext().prec = digits
    total = (3)
    last = total
    a = (2)
    b = (3)
    c = (4)
    def added(a,b,c):
        return (4/(a*b*c))
    while total < math.pi:
        total += (added(a,b,c) - added(a+2,b+2,c+2))
        a+= 4
        b+= 4
        c+= 4
        if last == total:
            return total
        last = total
    #return total.__round__(digits)

def findpi_ramanujun():
    """
    Uses Ramanujun equation to find pi to digits number of digits - not right amount of digits
    :return: pi
    """
    from decimal import Decimal, getcontext
    import math
    digits = 30
    getcontext().prec = digits
    final_loop = 10
    sumnum = 0
    for k in range(final_loop):
        oldsum = sumnum
        sumnum += ((math.factorial(4*k))*(1103+26390*k))/(math.factorial(k)*(396**(4*k)))
        if oldsum == sumnum:
            break
    return 1/(((2*math.sqrt(2))/9801)*sumnum)

def find_pi2():
    from decimal import Decimal, getcontext
    # print('How many decimal places do you want? :', end=' ')
    #places = input()
    places = 30
    getcontext().prec = places
    m = 10

    a = [0]*m
    b = [0]*m
    t = [0]*m
    p = [0]*m

    one = Decimal(1)
    two = Decimal(2)
    four = Decimal(4)
    half = one/two

    a[0] = one
    b[0] = one/two**(one/two)
    t[0] = one/four
    p[0] = one

    lastpi = 0

    for n in range(m-1):
        a[n+1] = (a[n]+b[n])/two
        b[n+1] = (a[n]*b[n])**half
        t[n+1] = t[n] - p[n]*(a[n]-a[n+1])**2
        p[n+1] = two*p[n]

        pi = (a[n+1] + b[n+1])**2/four/t[n+1]
        if lastpi == pi:
            break
        lastpi = pi
    return pi
    #print('Pi calculated in', n, 'loops, as', pi)

def findpi3():
    from decimal import Decimal, getcontext

    # credit for this algorithm goes to Chris Hills
    # http://www.codeproject.com/Articles/11692/Calculate-pi-to-one-million-decimal-places

    def calc_pi(precision = 30):

        pi = Decimal(4) * (Decimal(4) * inverse_tangent(Decimal(1)/Decimal(5), precision + 2) - inverse_tangent(Decimal(1)/Decimal(239), precision + 2))

        l = list(str(pi))
        l.pop()
        l.pop()
        new_pi = ''.join(l)

        return new_pi

    def inverse_tangent(value, precision):
        i = 0
        getcontext().prec = precision
        result = Decimal(0)
        s = Decimal(1)

        while True:
            old_result = result
            x = Decimal(2*i + 1)
            result += Decimal(s*((value**x)/x))
            s *= Decimal(-1)
            i += 1
            if old_result == result:
                break

        return result

    print(calc_pi())

if __name__ == "__main__":
    import math
    #r = 4
    #area = math.pi * r**2
    #print(findpi(r,area))
    print(findpi_infseries())
    print(find_pi2())
    # print(findpi3())
    print(findpi_ramanujun())