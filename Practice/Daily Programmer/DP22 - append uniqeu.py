__author__ = 'Stuart'
"""
Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.
input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
output: ["a", "b", "c",1,4,"x",34, "4"]
http://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/
"""
def append_unique(L1,L2):
    return L1 + [item for item in L2 if item not in L1]

if __name__ == "__main__":
    L1 = ["a","b","c",1,4,]
    L2 = ["a", "x", 34, "4"]
    print(append_unique(L1,L2))
    for thing in L2:
        if thing not in L1:
            L1.append(thing)
    print(L1)