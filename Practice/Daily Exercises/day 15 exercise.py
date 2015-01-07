"""Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx1234567890~!@#$%^&*()-_=+[{]}\|;:,<.>/?"
wordlist = ["bread", "glory", "banana", "china", "shanghai", "equestrian", "popular", "bose", "pills", "yourname","hooray"]


def strength(): #gets strength of user's desired password
    confirm = input("Do you want a strong or weak password?").lower()
    if confirm == "strong":
        return True
    elif confirm == "weak":
        return False
    else:
        print("Sorry, wasn't sure what you said... Can you repeat that?")
        strength()


def password_generator():
    password = ""
    if strength():
        for i in range(16): #if they want a strong password, do 16 random characters. Can repeat
            password += (random.choice(alphabet))
    else:
        for i in range(3): #if they want a weak, have three words with no spaces in between
            password += random.choice(wordlist)
    return password


print("Your password is", password_generator())
