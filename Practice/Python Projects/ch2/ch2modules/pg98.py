__author__ = 'Stuart'

def ignore_pyc(root,names):
    """
    pyc files are compiled python files
    :param root:
    :param names:
    :return:
    """
    return [name for name in names if name.endswith('pyc')]

import shutil as sh

ignore_pyc('fred',['1.py','2.py','2.pyc','4.py','5.pyc'])
sh.copytree('projdir','projbak',ignore=ignore_pyc)