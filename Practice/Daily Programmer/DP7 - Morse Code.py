__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
Write a program that can translate Morse code in the format of ...---...
A space and a slash will be placed between words. ..- / --.-
For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.
This is your Morse to translate:
.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

image with code in file
"""

encrypt = {'A':'.-', 'B':'-...',"C":'-.-.', "D":"-..","E":'.','F':'..-.','G':"--.",'H':'....',"I":'..',"J":'.---',
           "K":'-.-',"L":'.-..',"M":'--', "N":"-.",'O':'---','P':'.--.','Q':'--.-','R':'.-.',"S":'...',"T":"-","U":"..-","V":"...-",
           "W":'.--',"X":'-..-',"Y":"-.--","Z":"--..",'1':'.----','2':'..---',"3":'...--',"4":'....-',"5":'.....',
           '6':'-....',"7":'--...',"8":'---..',"9":'----.',"0":"-----", " ": "/"}
decrypt = {v:k for k,v in encrypt.items()}

def decrypter(phrase):
    splitphrase = phrase.split()
    for i in range(len(splitphrase)):
        if splitphrase[i] in decrypt:
            splitphrase[i] = decrypt[splitphrase[i]]
    return ''.join(splitphrase)

def encrypter(phrase):
    """
    easier way of doing this by adding to a new string
    :param phrase: english phrase
    :return: morse phrase
    """
    newphrase = ''
    for letter in phrase:
        newphrase += encrypt[letter] + " "
    return newphrase

def makenoise(morsecode):
    import winsound
    import time
    Freq = 2500 # Set Frequency To 2500 Hertz
    dot_duration_inms = 50 #Set Duration To 1000 ms == 1 second
    for character in morsecode:
        if character == '.':
            winsound.Beep(Freq,dot_duration_inms)
        elif character == '-':
            winsound.Beep(Freq-500,dot_duration_inms*2)
        time.sleep(dot_duration_inms*4/1000)

if __name__ == "__main__":
    decryptphrase = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
    encryptphrase = "I HATE CAPITAL LETTERS"
    # print(decrypter(decryptphrase))
    # print(encrypter(encryptphrase))
    # #print(decrypter(encrypter(encryptphrase)))
    makenoise(encrypter(encryptphrase))
