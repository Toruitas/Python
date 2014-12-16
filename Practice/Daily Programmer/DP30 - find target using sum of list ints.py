__author__ = 'Stuart'
"""
Write a program that takes a list of integers and a target number and determines if any two integers in the list sum
to the target number. If so, return the two numbers. If not, return an indication that no such integers exist.
http://www.reddit.com/r/dailyprogrammer/comments/reago/3262012_challenge_30_easy/

sounds kind of like the penny problem

Bad efficiency: for each individual integer, go through the list twice (for i & for j) to see if they add up.

Better: sort, then do above. If > target, return False

Better: use a tree. Depth or breadth... not sure.
"""

def bad(list,target):
    """
    O n **2 complexity.
    :param list:
    :param target:
    :return:
    """
    for i in list:
        for j in list:
            if i + j == target:
                return i, j
    return False

def better(list,target):
    """
    same as above but sorted, so can cut some processing out. Still inefficient.
    :param list:
    :param target:
    :return:
    """
    list = sorted(list)
    for i in list:
        for j in list:
            if i + j > target:
                break
            elif i + j == target:
                return i, j
    return False

def checksum(num_list, target):
    """
    using list comprehensions / generators
    :param num_list:
    :param target:
    :return:
    """
    solutions = []
    solutions.append([(x, y) for x in num_list for y in num_list if x + y == target])
    return solutions

def iter():
    import itertools

    def pairs_with_sum(list, n):
        pairs = itertools.permutations(list, 2)
        return (p for p in pairs if sum(p) == n)

    def has_sum(list, n):
        try:
            return pairs_with_sum(list, n).next()
        except StopIteration:
            return None

def clever():
    """
    (Where A and B are the two numbers to be summed, and B > A)
SORT the integers into smallest -> biggest
FIND the smallest number, when doubled is larger than the target
    SET B to this number.
SET A to the number on the left of B.
LOOP UNTIL A+B equals the target
    IF A+B is Greater than the target THEN, MOVE A to the left
        IF A cannot be moved to the left, END - NO SOLUTION
    IF A+B is Less than the target THEN, MOVE B to the right
        IF B cannot be moved to the right, END - NO SOLUTION
RETURN A and B
    :return:
    """
    from time import clock

    target = int(input("Enter a target num:"))
    start = clock()

    nums = sorted(range(150,500) + range(1000,2000,2) + range(100))     #random big list
    a = b = loops = i =  0
    noSolution = False

    try:
        while b <= int(target/2):
            b = nums[i]
            i+= 1
    except:
        noSolution = True

    bIndex = nums.index(b)
    aIndex = bIndex-1
    a = nums[aIndex]

    while a+b != target and not noSolution:
        loops += 1
        if a+b > target:
            if aIndex > 0:
                aIndex -= 1     #print "shifting a to next lower value"
                a = nums[aIndex]
            else:
                noSolution = True
        else:
            if bIndex < len(nums)-1:
                bIndex += 1     #print "shifting b to next higher value"
                b = nums[bIndex]
            else:
                noSolution = True

    if noSolution:
        print("No solution possible")
    else:
        print(a,"+",b,"=",target)

    print("no of loops:",loops)
    print(clock()-start,"s")