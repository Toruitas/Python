__author__ = 'Stuart'

# Problem 2: Unit test for P1

import unittest
from Boson import problem_one
class BooleanTestCase(unittest.TestCase):
    """test for utility_function"""

    def test_problem_one(self):
        self.assertTrue(problem_one("banana","banana"))
        self.assertTrue(problem_one("banana","ananab"))
        self.assertFalse(problem_one("a","bbbbbbbb"))
        self.assertTrue(problem_one("ichwh", "which"))
        self.assertFalse(problem_one("ichic","which"))
        self.assertTrue(problem_one("",""))
        self.assertFalse(problem_one("","a"))

if __name__=="__main__":
    unittest.main()