__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/
Input: list of elements and a block size k or some other variable of your choice
Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.
For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.
"""
def blocky_reverse(elements, blockSize=2):
    result = []
    pos = 0
    while(pos < len(elements)):
        result.extend(reversed(elements[pos:pos + blockSize]))
        pos += blockSize
    return result

def blocky_reverse_b(elements,blocksize = 2):
    result = []
    for pos in range(0,len(elements),blocksize):
        result.extend(reversed(elements[pos:pos+blocksize]))
    return result

def reversed_blocks(iterable, size=2):
    import itertools
    args = [iter(iterable)] * size #makes it an iterable, times 2
    blocks = itertools.zip_longest(*args)
    blocks_reversed = map(reversed, blocks)  # uses given function(reversed) on an iterable
    return itertools.chain.from_iterable(blocks_reversed)

def reverse_blocks_recursive(L, blocksize=2):
    if len(L)<blocksize:
        return L
    else:
        return list(L[:blocksize])[::-1] + reverse_blocks_recursive(L[blocksize:],blocksize)
    #  have to make the first block a separate list before you can reverse it

def reverse_block(L):
    return L[::-1]

if __name__ == "__main__":
    # blocksize = 3
    # list1 = [12, 24, 32, 44, 55, 66]
    # templist = []
    # revlist = []
    # start = 0
    # end = blocksize
    # while end <= len(list1):
    #     templist = list1[start:end]
    #     revlist.extend(reverse_block(templist))
    #     start += blocksize
    #     end += blocksize
    # print(revlist)
    print(blocky_reverse_b([12, 24, 32, 44, 55, 66,88,0],2))
    print(list(reversed_blocks([12, 24, 32, 44, 55, 66,88,0])))
    print(reverse_blocks_recursive([12, 24, 32, 44, 55, 66,88,0]))