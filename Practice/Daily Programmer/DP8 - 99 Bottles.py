__author__ = 'Stuart'
"""
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall...

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall...

http://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
"""

for i in range(99,2,-1):
    print(i," bottles of beer on the wall,", i, "bottles of beer. \n"
                                                "Take one down, pass it around,", i-1, " bottles of beer on the wall.")

print("2 bottles of beer on the wall, 2 bottles of beer. \n"
      "Take one down, pass it around, 1 bottle of beer on the wall.\n"
      "1 bottle of beer on the wall, one last bottle of beer. \n"
      "Take it down, pass it around, no more bottles of beer on the wall \n"
      "No more bottles of beer on the wall, no more bottles of beer.\n"
      "Go to the store and buy some more, 99 bottles of beer on the wall.")