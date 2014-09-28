__author__ = 'Stuart'
"""
Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!

http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/.

Before I knew about .encode('rot13')...
https://docs.python.org/3.4/howto/unicode.html
"""

import random

capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def encrypt(phrase, shift = random.randint(1,26)):
    """
    Encrypt takes a user-defined phrase, and encrypts it according to a caesar cypher. Simple shift of the letters
    :param phrase: user-defined phrase to encrypt
    :param shift: user-defined shift, default random shift
    :return: shifted phrase
    """
    encrypted = ""
    for letter in phrase:
        if letter in capitals:
            encrypted += capitals[capitals.index(letter)+shift] #adds shifted capitals
        elif letter in lowers:
            encrypted += lowers[lowers.index(letter)+shift] #adds shifted lowers
        else:
            encrypted += letter
    return encrypted

def decrypt(phrase,wordList):
    """
    Takes a phrase the user would like to decrypt, decrypts it, and returns it
    :param phrase:
    :return: decrypted phrase
    Has to test to see if it actually a caesar cipher
    """
    key = 1
    acceptable_ratio = .75
    successes = 0
    while successes / len(phrase.split()) < acceptable_ratio:
        successes = 0
        #azmzmz azmzmz banana
        shifted = encrypt(phrase,key)
        shiftedlist = shifted.split(' ')
        for word in shiftedlist:
            if word.lower() in wordList:
                successes +=1
        if key > 25:
            break
        else:
            key +=1
    if successes / len(phrase.split()) > acceptable_ratio:
        return ''.join(shifted)

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Necesary for cipher testing
    """
    #print("Loading word list from file...")
    WORDLIST_FILENAME = "words.txt"
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList

if __name__ == "__main__":
    prompt = input("E for encrypt; D for decrypt")
    if prompt == "E":
        phrase = input("What phrase do you want to encrypt?")
        key = input("Type an integer between 1-26 that you want to use as the key. Otherwise, enter anything else for a random key.")
        try:
            if int(key) in range(1,27):
                print(encrypt(phrase,int(key)))
        except:
            print(encrypt(phrase))

    elif prompt == "D":
        print(decrypt(input("What is the phrase you want decrypted?"),loadWords()))
    else:
        print("Invalid input. Logging off.")
