"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
My name is Michele
Then I would see the string:
Michele is name My
shown back to me."""

sentence = input("What sentence would you like reversed?")
sentence1 = "My name is Michele"


def split_sentence(sentence):
    return sentence.split() #if you leave .split() empty, splits along whitespace. If filled with string, splits along string


def reverse_sentence_list(sentencelist):
    return sentencelist[::-1] #reverse the list


def rejoin_list(reversedlist):
    return " ".join(reversedlist) #Join list with string in the middle of each item


def reverse_sentence(sentence):
    return rejoin_list(reverse_sentence_list(split_sentence(sentence)))

#or


def reverse_sentence_short(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_sentence_short(sentence1))