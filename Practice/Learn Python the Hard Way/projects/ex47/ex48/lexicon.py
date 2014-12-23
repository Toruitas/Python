__author__ = 'Stuart'


lexicon = {
    'direction': ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest', 'down', 'up',
                  'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat', 'drink', 'sing', 'shoot','open'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it', 'on', 'through', 'a'],
    'noun': ['door', 'bear', 'princess', 'cabinet', 'beer', 'gun', 'sword', 'tits', 'muffin']
    #'numbers': '0123456789'
}

VOCABULARY = {value:key for key, word in lexicon.items() for value in word}
VOCABULARY_CLEAR = {word:direction for direction, list in lexicon.items() for word in list}
# for value in word refers to value in list.
# the list is word
# .items() returns an iterator of key:value pairs
# turns words in the list into keys, with directions as the values. An unpacking.


def scan(sentence):
    """
    From a sentence, break it down, attach type of word based on VOCABULARY, and return list of tuples
    :param sentence: a string
    :return: list of tuples
    """
    tokens = []
    for word in sentence.split():
        lowered = word.lower()
        # lower it independently each time so wer can return the original word with original casing.
        try:
            word_type = VOCABULARY[lowered]  # tries to use word as a key to get its type
        except KeyError:  # if it's not in there, try to convert it to a number
            try:
                value = int(word)
            except ValueError:
                tokens.append(('error', word))  # if it's not a number, either, it is an error
            else:
                tokens.append(('number', value))  # (number, number value)
        else:
            tokens.append((word_type, word))  # (type, word)
    return tokens


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

