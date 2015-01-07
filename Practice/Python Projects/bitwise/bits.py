__author__ = 'Stuart'

"""
In this Try It Out, you start out by creating a simple, conventional module based on integer inputs.
You then create another module that defines a class that can be used to represent a piece of binary
data and expose the bitwise functions as methods. Finally, you create a package containing both
modules.
"""

#! /bin/env python3
"""
functional wrapper around the bitwise operators.
Designed to make their use more intuitive to users not
familiar with the underlying C operators.
Extends the functionality with bitmask read/set operations

The inputs are integer values and
return types are 16 bit integers or boolean.
Bit indexes are zero based

Functions implemented are:
NOT(int)                -> int
AND(int, int)           -> int
OR(int, int)            -> int
XOR(int, int)           -> int
shiftleft(int, num)     -> int
shiftright(int, num)    -> int
bit(int, index)         -> bool
setbit(int, index)      -> int
zerobit(int, index)     -> int
listbits(int, num)      -> [int, int, ..., int]
"""

def NOT(value):
    """
    ~
    :param value:
    :return:
    """
    return ~value

def AND(val1, val2):
    return val1 & val2

def OR(val1, val2):
    return val1 | val2

def XOR(val1, val2):
    """
    A bitwise XOR takes two bit patterns of equal length and performs the logical exclusive
    OR operation on each pair of corresponding bits
 The result in each position is 1 if only the first bit is 1 or only the second bit is
 1, but will be 0 if both are 0 or both are 1. In this we perform the comparison of two
  bits, being 1 if the two bits are different, and 0 if they are the same.

    Look at this example vertically:
        0101 (decimal 5)
    XOR 0011 (decimal 3)
      = 0110 (decimal 6)
    :param val1:
    :param val2:
    :return:
    """
    return val1 ^ val2

def shiftleft(val, num):
    return val << num

def shiftright(val, num):
    return val >> num

def bit(val, idx):
    mask = 1 << idx  # all 0 except idx. idx is index
    return bool(val & mask)

def setbit(val, idx):
    """
    'setting a bit' means making its value 1.
    :param val:
    :param idx:
    :return:
    """
    mask = 1 << idx  # all 0 except idx
    return val | mask

def zerobit(val, idx):
    """
    AKA resetting a bit.
    :param val:
    :param idx:
    :return:
    """
    mask = ~(1 << idx)  # all 1 except idx
    return val & mask

def listbits(val):
    """
    bin converts a valid integer to a binary string
    :param val:
    :return:
    """
    num = len(bin(val)) - 2  # -2 to account for leading 0b characters
    result = []
    for n in range(num):
        result.append(1 if bit(val, n) else 0)
    return list(reversed(result))