__author__ = 'Stuart'
"""
write a program that will allow the user to input digits, and arrange them in numerical order.
for extra credit, have it also arrange strings in alphabetical order
"""

if __name__ == "__main__":
    userinput = input("Enter some numbers. I recommend including 42 at least once for the answer to the meaning if the universe.")
    splitinput = userinput.split()
    splitinput.sort()
    print(" ".join(item for item in splitinput))