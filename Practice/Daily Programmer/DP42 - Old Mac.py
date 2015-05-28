__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/sobna/4232012_challenge_42_easy/

Write a program that prints out the lyrics for "Ninety-nine bottles of beer", "Old McDonald had a farm" or "12 days of
Christmas".
If you choose "Ninety-nine bottles of beer", you need to spell out the number, not just write the digits down. It's
"Ninety-nine bottles of beer on the wall", not "99 bottles of beer"!

For Old McDonald, you need to include at least 6 animals: a cow, a chicken, a turkey, a kangaroo, a T-Rex and an animal
of your choosing (Old McDonald has a weird farm). The cow goes "moo", the chicken goes "cluck", the turkey goes "gobble"
, the kangaroo goes "g'day mate" and the T-Rex goes "GAAAAARGH". You can have more animals if you like.

Make your code shorter than the song it prints out!
"""

def old_mac():
    animals = {'cow':'moo','chicken':'cluck','turkey':'gobble','kangaroo':"g'day mate",'T-Rex':'GAAAARGH'}
    for animal, sound in animals.items():
        print("Old MacDonald had a farm\nEIEIO")
        print("And on this farm he had a {}\nEIEIO".format(animal))
        print("With a {} {} here\n".format(sound,sound),
              "and a {} {} there\n".format(sound,sound),
              "Here a {}, there a {}\n".format(sound,sound),
              "Everywhere a {} {}.\n".format(sound,sound))
        print("Old MacDonald had a farm, EIEIO")

old_mac()