__author__ = 'Stuart'

def f(x):
    for x in range(x):
        yield x ** 3

for x in f(5):  # f(x) is an iterator, yield helps it remember where it left off. saved on yield, restored on next
                # returns gen obj
    print(x)
# 0 1 8 27 64

def build_string():
    """01234567891011"""
    return ''.join(str(x) for x in range(101))

def print_contents():
    try:
        with open("text.txt",'r') as file:
            print(file.read())
    except IOError:
        print("No file found")

#print(build_string.__doc__)
#print_contents()

lamb1 = lambda x: x**3
print(lamb1(5))
lamb2 = lambda x: x%2
print(lamb2(3))

