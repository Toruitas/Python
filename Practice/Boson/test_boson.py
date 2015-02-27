__author__ = 'Stuart'

# Problem 2: Unit test for P1

import unittest
from Boson import no_name, utility_function, utility_function_2
class BooleanTestCase(unittest.TestCase):
    """test for utility_function"""
    def test_utility_functions(self):
        self.assertEqual(utility_function("banana",0), 'anana')
        self.assertEqual(utility_function_2("banana",0), 'anana')
        self.assertEqual(utility_function("test1",4), 'test')
        self.assertEqual(utility_function_2("test1",4), 'test')
        self.assertEqual(utility_function_2("asdjfioawefi",7), utility_function("asdjfioawefi",7))
        self.assertEqual(utility_function("a",0),"")
        self.assertEqual(utility_function_2("a",0), "")
        self.assertEqual(utility_function("",0), "")
        self.assertEqual(utility_function_2("",0), "")
        self.assertEqual(utility_function("",0), utility_function_2("",0))

    def test_no_names(self):
        self.assertTrue(no_name("banana","banana"))
        self.assertTrue(no_name("banana","ananab"))
        self.assertFalse(no_name("a","bbbbbbbb"))
        self.assertTrue(no_name("ichwh", "which"))
        self.assertFalse(no_name("ichic","which"))
        self.assertTrue(no_name("",""))
        self.assertFalse(no_name("","a"))

if __name__=="__main__":
    unittest.main()