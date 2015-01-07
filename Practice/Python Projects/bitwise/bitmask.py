__author__ = 'Stuart'

#! /bin/env python3
"""
Class that represents a bit mask.
It has methods representing all
the bitwise operations plus some
additional features. The methods
return a new BitMask object or
a boolean result. See the bits
module for more on the operations provided.
"""

class BitMask(int):
    def AND(self,bm):
        """Does a "bitwise and". Each bit of the output is 1 if the corresponding
        bit of x AND of y is 1, otherwise it's 0."""
        return BitMask(self & bm)

    def OR(self,bm):
        """
        Does a "bitwise or". Each bit of the output is 0 if the corresponding
         bit of x AND of y is 0, otherwise it's 1.
        :param bm:
        :return:
        """
        return BitMask(self | bm)

    def XOR(self,bm):
        """
        Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in
        y is 0, and it's the complement of the bit in x if that bit in y is 1.
        :param bm:
        :return:
        """
        return BitMask(self ^ bm)

    def NOT(self):
        """
        Returns the complement of x - the number you get by switching each 1
        for a 0 and each 0 for a 1. This is the same as -x - 1.
        :return:
        """
        return BitMask(~self)

    def shiftleft(self,num):
        return BitMask(self << num)

    def shiftright(self,num):
        return BitMask(self >> num)

    def bit(self, num):
        mask = 1 << num
        return bool(self & mask)

    def setbit(self, num):
        mask = 1 << num
        return BitMask(self | mask)

    def zerobit(self, num):
        mask = ~(1 << num)
        return BitMask(self & mask)

    def listbits(self, start=0, end=-1):
        end = end if end < 0 else end + 2
        return [int(c) for c in bin(self)[start+2:end]]