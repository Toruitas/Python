__author__ = 'Stuart'

"""
http://www.reddit.com/r/dailyprogrammer/comments/srowj/4252012_challenge_44_easy/

Write a program that divides up some input text into sentences and then determines which sentence in the input has the
most words. Print out the sentence with the most words and the number of words that are in it. Optionally, also print
out all words in that sentence that are longer than 4 characters.
Sentences can end in periods, exclamation points and question marks, but not colons or semi-colons.
"""

def divide(text):
    sents = []

    def splits(text):
        puncutation_index = min(text.index("?"),text.index("!"), text.index("."))  # need to look up this one.
        sents.append(text[:puncutation_index])
        splits(text[puncutation_index:])

    def words(sentence):
        return len(sentence.split())

    splits(text)
    sents = [(words(sent),sent) for sent in sents]

    length = 0
    sentence = ''
    for s in sents:
        if s[0] > length:
            length = s[0]
            sentence = s[1]

    print(sentence, length)

def two(text):
    import re

    rank = [ s.split(" ") for s in re.split("[\.!\?] ", text) ]
    rank.sort(key=lambda x: len(x),reverse=True)
    print("{} : {}.".format(len(rank[0]), ' '.join(rank[0])))
    print([ x for x in rank[0] if len(x) >= 4 ])

with open('DP44.txt') as file:
    text = file.read()
    two(text)


# def four(text):
#     s = []
#
#     for line in open('text.txt').readlines():
#         line = line.replace('!', '.')
#         line = line.replace('?', '.')
#         s = s + line.split('.')
#
#     max_words = 1
#     index_max = 0
#     for i in range(len(s)):
#         if max_words < len(s[i].split()):
#                 max_words = len(s[i].split())
#                 index_max = i
#
#     print s[index_max]
#     for word in s[index_max].split():
#          if len(word.replace(',', '')) > 4:
#                 print word.replace(',', '')