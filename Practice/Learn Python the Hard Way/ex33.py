__author__ = 'Stuart'

def loopty(max,step):
    i = 0
    numbers = []

    while i <max:
        print("At the top i is {}".format(i))
        numbers.append(i)
        i += step
        print("Numbers now: ",numbers)
        print("At the bottom i is {}".format(i))

    print("The numbers: ")
    for num in numbers:
        print(num)

def loopty_for(max,step):
    numbers = []
    for i in range(0,max,step):
        print("At the top i is {}".format(i))
        numbers.append(i)
        print("Numbers now: ",numbers)
        print("At the bottom i is {}".format(i))

    print("The numbers: ")
    for num in numbers:
        print(num)