__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/ruiob/452012_challenge_36_easy/
1000 Lockers Problem.
In an imaginary high school there exist 1000 lockers labelled 1, 2, ..., 1000. All of them are closed. 1000 students are to "toggle" a locker's state. * The first student toggles all of them * The second one toggles every other one (i.e, 2, 4, 6, ...) * The third one toggles the multiples of 3 (3, 6, 9, ...) and so on until all students have finished.
To toggle means to close the locker if it is open, and to open it if it's closed.
How many and which lockers are open in the end?
"""
nums = [1,2,3,4,5]
print(' '.join(str(n) for n in nums))