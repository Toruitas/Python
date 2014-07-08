#day 2 practice.py

"""Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user."""

number = int(raw_input("What is your number?"))
check = int(raw_input("What do you want to check it against?"))

if number%4==0:
    print "Divisible by 4, also even"
elif number%2==0:
    print "Even"
else:
    print "Odd"

if number%check==0:
    print "Yep, divides evenly"
else:
    print "Does not divide evenly"