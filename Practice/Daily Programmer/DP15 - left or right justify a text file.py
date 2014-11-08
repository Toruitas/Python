__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
Write a program to left or right justify a text file

http://stackoverflow.com/questions/16604826/python-read-write-text-file
"""
def sysarg_vers():
    """
    Not sure what this is supposed to do...
    :return:
    """
    import sys
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            if sys.argv[2].lower() == '-l':
                print ('{:<' + sys.argv[3] + '}').format(line.lstrip().rstrip())
            elif sys.argv[2].lower() == '-r':
                print ('{:>' + sys.argv[3] + '}').format(line.lstrip().rstrip())

if __name__ == "__main__":
    import shutil
    with open("DP15.txt", "r") as old, open("DP15a.txt","w") as new:
    #  r read only, w write only, a append (any data added directly to end), r+ for r&w. r assumed
        for line in old:
            new.write(str.rjust(line,50,"0"))
    shutil.move("DP15a.txt","DP15.txt")
    with open("DP15.txt") as file:
        for line in file:
            print(len(line))