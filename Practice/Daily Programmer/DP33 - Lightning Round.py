__author__ = 'Stuart'
"""
This would be a good study tool too. I made one myself and I thought it would also be a good challenge.
Write a program that prints a string from a list at random, expects input, checks for a right or wrong answer, and keeps
 doing it until the user types "exit". If given the right answer for the string printed, it will print another and
 continue on. If the answer is wrong, the correct answer is printed and the program continues.
Bonus: Instead of defining the values in the program, the questions/answers is in a file, formatted for easy parsing.
Example file:
12 * 12?,144
What is reddit?,website with cats
Translate: hola,hello
http://www.reddit.com/r/dailyprogrammer/comments/rl24e/3302012_challenge_33_easy/

TODO:
Add a flag for repeating questions, so that you can do a single randomized run through the list of Q's
"""

def load_QA(source=None):
    if source:
        import csv
        with open(source) as csv_file:
            reader = csv.reader(csv_file)
            test_list2 = [(row[0],row[1]) for row in reader]
        print(test_list2)
        return test_list2
    else:
        test_list = [("What's the color of the sky?","blue"),
            ("How many letters are in 'stu?'","3"),
            ("What is the airspeed of an unladen swallow?","2lbs"),
            ("Who is the president?","Obama")]
        return test_list


def test(source,continuous=False):
    import random
    to_ask = [i for i in range(len(source))]
    while True:
        if len(to_ask) == 0:
            print("All questions reviewed.")
            break
        rand_ind = random.choice(to_ask)
        # rand_ind = random.randint(0, len(source)-1)
        A = input(source[rand_ind][0])
        if A == "exit":
            break
        elif A == source[rand_ind][1]:
            print("Correct")
            if not continuous:
                to_ask.remove(rand_ind)
        else:  #  A != source[rand_ind][1]:
            print("Wrong, {}".format(source[rand_ind][1]))

if __name__ == "__main__":
    src = "DP33.csv"
    test(load_QA(src))

def qa(filename):
    questions = {}

    #Load the questions file
    try:
        with open(filename) as f:
            for line in f:
                if line.strip():
                    question, answer = line.lower().rsplit(',', 1)
                    questions[question.strip()] = answer.strip()
    except IOError:
        pass

    keys = questions.keys()

    if not keys:
        print('No questions loaded')
        return False

    #Main Q&A loop
    while True:
        if not keys:
            print('All questions used, repeating')
            keys = questions.keys()

        #Select a question (without replacement)
        import random
        i = random.randrange(0, len(keys))
        answer = questions[keys[i]]
        print(keys[i])
        del keys[i]

        #Evaluate user answer
        guess = input('>>> ').lower().strip()
        if guess in ('q', 'quit', 'exit'):
            break
        if guess == answer:
            print('Correct!')
        else:
            print('Incorrect! The correct answer is:')
            print('  ' + answer)

    return True

if __name__ == '__main__':
    #Sample file
    qa('questions.txt')


def study():
    repeat ='yes'
    while repeat == 'yes' or repeat =='y':
        questions={}
        with open('qanda.txt','r') as f:
            for line in f:
                q=line.split(',')
                questions[q[0]]=q[1].strip('\n')
        from random import choice
        try:
            while repeat!='quit':
                quest = choice(list(questions))
                repeat = input(quest+' ')
                if questions[quest]==repeat:
                    print(True)
                    del questions[quest]
                elif repeat =='quit':
                    print('Quitting Program.')
                    repeat='no'
                else:
                    print(False,'. The correct answer is: ',questions[quest],sep='')
        except IndexError:
            print('Answered all the questions correctly. No more questions!')
            repeat = input('Repeat?: ')
            while repeat not in ['yes','no','quit','y','n']:
                repeat = input('Please respond with yes or no! Repeat?')