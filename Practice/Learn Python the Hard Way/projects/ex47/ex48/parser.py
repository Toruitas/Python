__author__ = 'Stuart'


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember, we take ('noun','princess') tuples and save them
        # subject, verb, object are all tuples
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    """
    Identify the next word with peek.
    From a word list, peeks at the first word.
    :param word_list: list of words
    :return: type of first word in that list
    """
    if word_list:
        word = word_list[0]  # get tuple for word
        return word[0]  # return type of word -- not a tuple
    else:
        return None


def match(word_list, expecting):
    """
    From word list, removes first word and compares it to what we were expecting.
    If it is the same, returns it.
    Otherwise, returns None
    :param word_list:
    :param expecting:
    :return: expected word or None
    """
    if word_list:
        word = word_list.pop(0)  # pops off the first tuple ('direction','north) or ('verb', 'go')
        if word[0] == expecting:  # 'direction' == 'direction'
            return word  # returns tuple if it is of the type expected
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """
    As long as the type returned by peek matches given word type,
    runs match on the list to pop that word off to skip it, I guess.
    :param word_list:a list of phrase tuples?
    :param word_type:
    :return: nothing, just processes the list
    """
    while peek(word_list) == word_type:  # 'stop' == 'stop'
        match(word_list, word_type)  # does the thing


def parse_verb(word_list):
    """
    uses skip on 'stop' words to skip them and get to a verb
    :param word_list: sentence, broken down into list
    :return: tuple: verb
    """
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')  # should look like ('verb','go')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    """
    uses skip('stop') to skip to next key word, which then peeks at next word, and matches if it should
    :param word_list:
    :return: tuple noun:word or noun:direction
    """
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')  # returns noun tuple ('noun','bear')
    elif next == 'direction':
        return match(word_list, 'direction')  # returns direction tuple ('direction','north')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
    """
    takes word list, subject, verb, and object and creates a sentence object
    :param word_list: list of tuples, minus subject if start was a noun
    :param subj:
    :return:
    """
    verb = parse_verb(word_list)  # ('verb','go')
    obj = parse_object(word_list)  # ('noun', 'princess') or ('direction', 'north')

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')  # skips any opening nonsense stop words
    start = peek(word_list)  # peeks at first relevant word
    if start == 'noun':
        subj = match(word_list, 'noun')  # subject tuple, also pops from list
        return parse_subject(word_list, subj)  # then creates sentence based off of subject
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb. Not: {}.".format(start))