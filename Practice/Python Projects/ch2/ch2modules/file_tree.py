__author__ = 'Stuart'

# file_tree.py module containing functions to assist
# in working with directory hierarchies.
# Based on the os.walk function

import os, re
import os.path as path

def find_files(pattern, base='.'):
    """
    os.walk(base) returns triplet: ([root,root2,...],[dir1,dir2,dir3,...],[f1,f2,f3...])
    dirs are the directories contained inside, and files are the files.
    Root is of course the file tree for the containing folder.
    :param pattern: Finds files under base based on pattern
    :param base: Walks the file system starting at base
    :return: a list of filenames matching pattern
    """

    regex = re.compile(pattern)
    matches = []
    for root, dirs, files in os.walk(base):
        for f in files:  # will process the multiple files from os.walk(base)[2]
            if regex.match(f):
                matches.append(path.join(root, f))
    return matches