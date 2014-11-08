__author__ = 'Stuart'

"""
file for regex practice
"""

# if __name__ == "__main__":
#     # import re
#     # strlist = ["I have a big white dick","I have a big white dick","I have a big white DICK","I have a mandick."]
#     # for s in strlist:
#     #     print(re.sub('dick$', 'schlong', s))
#     # print([i for i in range(2)])
#

def reversed_blocks(iterable, size=2):
    import itertools
    args = [iter(iterable)] * size #makes it an iterable, times 2
    blocks = itertools.zip_longest(*args)
    blocks_reversed = map(reversed, blocks)  # uses given function(reversed) on an iterable
    return itertools.chain.from_iterable(blocks_reversed)