__author__ = 'Stuart'

import sys
sys.path.insert(0,"C:\\Users\\Stuart\\Documents\\GitHub\\Python\\Practice\\Learn Python the Hard Way\\projects\\ex47")
from nose.tools import *
#import ex47
from ex48 import lexicon
from ex48 import parser
from game import Room


word_list = lexicon.scan('a bear eat muffin')  # = [('stop','a'),('noun','bear'),('verb','eat'),('noun','muffin')]
# here are 4 sentences broken down into word_list format
PHRASE_LIST = [lexicon.scan('stop bear'), lexicon.scan('princess shoot the gun'),lexicon.scan('open the cabinet'),
               lexicon.scan('banana the great')]



def test_peek():
    assert_equal(parser.peek(word_list), 'stop')
    assert_equal([parser.peek(s) for s in PHRASE_LIST], ['verb','noun','verb','error'])
    # peeks at each s in word_list


def test_match():
    assert_equal(parser.match(word_list,'stop'), ('stop','a'))  # (word_list,word_list[0][0]) 'stop'
    assert_equal([parser.match(s, s[0][0]) for s in PHRASE_LIST], [('verb','stop'),('noun','princess'),('verb','open'),
                                                                  ('error','banana')])
    force_exception = lexicon.scan('banana banana banana')
    assert_equal(parser.match(force_exception, 'noun'), None)
    # try to match a ('error','banana'),'noun'. 'error' & 'noun' mismatch, so should get None


def test_skip():
    assert_equal(parser.skip(word_list,'stop'),None)

# def test_parse_verb_fail():
#     assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_verb():
    word_list1 = "a stop bear"
    assert_equal(parser.parse_verb(word_list1), ('verb', 'stop'))
    assert_equal([parser.parse_verb(s) for s in PHRASE_LIST], [('verb','stop'),'Expected a verb next.',('verb','open'),
                                                                  'Expected a verb next.'])