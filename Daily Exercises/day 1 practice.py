"""Gets your current name and age, then tells you when you will turn 100 years old
as many times as you would like it to"""

currentYear = 2014 #sets current year

name = raw_input("What is your name?") #grabs your name
age = int(raw_input("What is your age?")) #grabs age and converts to int
deepThought = int(raw_input("How many times do you need to hear it?")) #asks how many times you want to hear it

year = currentYear + 100-age #calculates year you turn 100

for i in range(deepThought): #prints out that year as many times as you need it to, you sadistic fuck
    print name + ", you will turn 100 in the year " + str(year) + "\n"