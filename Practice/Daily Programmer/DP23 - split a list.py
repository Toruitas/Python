__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/quli5/3132012_challenge_23_easy/
Input: a list
Output: Return the two halves as different lists.
If the input list has an odd number, the middle item can go to any of the list.
Your task is to write the function that splits a list in two halves.
"""

def split_lists(list):
    return list[:int(len(list)/2)], list[int(len(list)/2):]

if __name__ == "__main__":
    print(split_lists([1,2,3,4,5,6,7,8]))
    c23_easy = lambda n: print(n[:len(n)//2], n[len(n)//2:]) #  note to self, learn how to Lambda
    c23_easy([1,2,3,4,5])