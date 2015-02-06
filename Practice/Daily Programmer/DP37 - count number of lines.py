__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
write a program that takes
input : a file as an argument
output: counts the total number of lines.
for bonus, also count the number of words in the file.
"""

def count_lines(filename):
    lines = 0
    words = 0
    with open(filename,'r') as file:
        for line in file:
            l = line.split()
            lines += 1
            words += len(l)
    print("The file {} has {} lines and {} words".format(filename,lines,words))

count_lines("DP29 - Palindrome.txt")