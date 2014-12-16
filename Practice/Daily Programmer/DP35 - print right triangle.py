__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/
Write a program that will take a number and print a right triangle attempting to use all numbers from 1 to that number.
Sample Run:
Enter number: 10
Output:
7 8 9 10
4 5 6
2 3
1
Enter number: 6
Output:
4 5 6
2 3
1
Enter number: 3
Output:
2 3
1
Enter number: 12
Output:
7 8 9 10
4 5 6
2 3
1
"""

def find_base(num):
    """
    Tests if the number is a viable triangle builder, and then returns the base for the triangle building
    :param num: number for triangle
    :return: base length of pyramid, plus the number to start printing at
    """
    starting_num = num
    base = 1
    while num > 0:  # goes through possible bases until we have exhausted our goal number: 1 23 456 78910
        num -= base
        base +=1
    if num == 0:  # we have a base appropriate to make a rt triangle, while using all the numbers.
        # base-1 since have an extra base+1 in the while loop
        return base-1,starting_num
    else:  # we don't have a full base. Maybe it is 3, but the previous tier was 5. So use previous tier.
        # base-2 since we have the extra base+1 from the while loop, and want the tier before that
        return base-2,starting_num+(num+1)


def build_base2(nums,base):
    if base == 1:
        return str(nums[0])
    else:
        return ' '.join(str(n) for n in nums[-base:])+"\n" + build_base2(nums[:-base], base - 1)

from math import sqrt

def print_triangle(n):

    maxnumber = (-1 + int(sqrt(1 + 8*n)))/2

    def print_core(rows, count=0):
        if rows > 0:
            upto = count + maxnumber - rows + 1
            print_core(rows-1, upto)
            print(' '.join([str(i) for i in range(count + 1,
                     upto + 1)]))
    print_core(maxnumber)


if __name__ == '__main__':
    for i in range(100):
        print('i = %d' % i)
        print_triangle(i)

def triangle(n):
    totalnumbers=0
    lastrow=1
    for i in range(1,n):
        if totalnumbers+i<=n:
            totalnumbers+=i
            lastrow=i
        else:
            break
    while lastrow >0:
        for i in range(totalnumbers-lastrow+1,totalnumbers+1):
            print(i,end =' ')
        totalnumbers -=lastrow
        lastrow -= 1
        print('')

if __name__ == "__main__":
    test_nums = [10,6,3,12]
    for n in test_nums:
        b , n = find_base(n)[0], find_base(n)[1] # (base, starting_number) tuple assignment
        nums = list(range(1,n+1))  # the building blocks, excluding 0
        print(build_base2(nums,b))