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

def find_dirs(pattern, base= '.'):
    """
    directory version of find_files
    :param pattern:
    :param base:
    :return:
    """
    regex = re.compile(pattern)
    matches = []
    for root, dirs, files in os.walk(base):
        for d in dirs:
            if regex.match(d):
                matches.append(path.join(root,d))
    return matches

def find_all(pattern, base='.'):
    """
    find all version of above two, using them
    :param pattern:
    :param base:
    :return:
    """
    matches = []
    matches.append(find_dirs(pattern, base) + find_files(pattern, base))

def apply_to_files(pattern, function, base='.'):
    """
    Applies a function parameter to all files matching the input pattern.
    You could for example use this function to remove all files matching a pattern,
    such as *.tmp, like this:
    file_tree.apply_to_files('.*\.tmp', os.remove, 'TreeRoot')
    :param pattern: regex pattern for files you want to work with
    :param function: the function to apply to files
    :param base: directory we want to work under
    :return:nothing
    """
    regex = re.compile(pattern)
    for root,dirs,files in os.walk(base):
        for f in files:
            if regex.match(f):
                function(f)