from hw1 import *
import unittest

class TestFns(unittest.TestCase):
    def setUp(self):
        self.m0 = [[]]
        self.m1 = [[0]] # diagonal, triangular
        self.m2 = [[1]] # diagonal, triangular
        self.m3 = [[1, 0], 
                   [0, 1]] # diagonal, triangular
        self.m4 = [[0, 0], 
                   [0, 0]] # diagonal, triangular
        self.m5 = [[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]] # neither
        self.m6 = [[1, 2, 3], 
                   [0, 5, 6], 
                   [0, 0, 9]] # upper tri
        self.m7 = [[1, 0, 0], 
                   [4, 5, 0], 
                   [7, 8, 9]] # lower tri
        self.m8 = [[1, 0, 0], 
                   [4, 5, 0], 
                   [-7, -8, -9]] # lower tri
        self.m9 = [[1, 0, 0], 
                   [5, 5, 0], 
                   [-7, -8, -9]] # lower tri
        self.m10 = [[1, 1, 0], 
                    [0, 5, 0], 
                    [0, 0, -9]] # upper tri
        self.m11 = [[1, 0], 
                    [0, 1], 
                    [0, 0]] # diagonal
        self.m12 = [[1, 0, 0], 
                    [0, 1, 0]] # diagonal
        self.m13 = [[1, 0], 
                    [0, 1], 
                    [0, 8]] # neither
        self.m14 = [[1, 0, 0], 
                    [0, 1, 8]] # neither
        self.m15 = [[1], 
                    [0], 
                    [3]] # neither
        self.m16 = [[1, 0, 3]] # neither               
        self.m17 = [[-45, -12, -13], 
                    [-14, -15, -16], 
                    [-17, -18, -9]] # neither
        self.m18 = [[-45, -12, -13], 
                    [-14, -15, -16], 
                    [-17, -18, -9]] # neither
        self.m19 = [[1, 1, 0], 
                    [-1, 5, 0], 
                    [0, 0, -9]] # neither
        self.m20 = [[1, 2, 3], 
                    [1, 5, 6], 
                    [0, -1, 9]] # not upper tri
        self.m21 = [[1, 0], 
                    [0, 1], 
                    [0, 0], 
                    [0, 8]] # neither
        self.m22 = [[1, 0, 0, 0], 
                    [0, 1, 0, 8]] # neither
        self.m23 = [[1, 0], 
                    [0, 1], 
                    [0, 0], 
                    [0, 0]] # diagonal
        self.m24 = [[1, 0, 0, 0], 
                    [0, 1, 0, 0]] # diagonal
        self.m25 = [[1, 0, 0, 0], 
                    [0, 1, 8, 0]] # neither
        self.m26 = [[9, 8], 
                    [0, 0]] # for second_biggest
        self.m27 = [[9], 
                    [0]] # for second_biggest
        self.m28 = [[9, 8]] # for second_biggest
        
    def test_is_diagonal(self):
        self.assertTrue(is_diagonal(self.m1))
        self.assertTrue(is_diagonal(self.m2))
        self.assertTrue(is_diagonal(self.m3))
        self.assertTrue(is_diagonal(self.m4))
        self.assertFalse(is_diagonal(self.m5))
        self.assertFalse(is_diagonal(self.m6))
        self.assertFalse(is_diagonal(self.m7))
        self.assertTrue(is_diagonal(self.m11))
        self.assertTrue(is_diagonal(self.m12))
        self.assertFalse(is_diagonal(self.m13))
        self.assertFalse(is_diagonal(self.m14))
        self.assertFalse(is_diagonal(self.m19))
        self.assertFalse(is_diagonal(self.m21))
        self.assertFalse(is_diagonal(self.m22))
        self.assertFalse(is_diagonal(self.m25))
        self.assertTrue(is_diagonal(self.m23))
        self.assertTrue(is_diagonal(self.m24))
        
    def test_is_upper_triangular(self):
        self.assertTrue(is_upper_triangular(self.m1))
        self.assertTrue(is_upper_triangular(self.m2))
        self.assertTrue(is_upper_triangular(self.m3))
        self.assertTrue(is_upper_triangular(self.m4))
        self.assertFalse(is_upper_triangular(self.m5))
        self.assertTrue(is_upper_triangular(self.m6))
        self.assertFalse(is_upper_triangular(self.m7))
        self.assertTrue(is_upper_triangular(self.m10))
        self.assertFalse(is_upper_triangular(self.m20))
        
    def test_contains(self):
        self.assertTrue(contains(self.m1, 0))
        self.assertFalse(contains(self.m1, 1))
        self.assertFalse(contains(self.m0, 0))
        self.assertFalse(contains(self.m0, 1))
        self.assertTrue(contains(self.m7, 0))
        self.assertTrue(contains(self.m7, 5))
        self.assertTrue(contains(self.m7, 9))
        self.assertTrue(contains(self.m7, 8))
        self.assertFalse(contains(self.m7, -1.3))
        self.assertTrue(contains(self.m13, 8))
        self.assertTrue(contains(self.m14, 8))
        self.assertTrue(contains(self.m21, 8))
        self.assertTrue(contains(self.m22, 8))
        self.assertTrue(contains(self.m25, 8))
       
    def test_biggest(self):
        self.assertEqual(0, biggest(self.m1))
        self.assertEqual(1, biggest(self.m3))
        self.assertEqual(9, biggest(self.m7))
        self.assertEqual(5, biggest(self.m8))
        self.assertEqual(3, biggest(self.m15))
        self.assertEqual(3, biggest(self.m16))
        self.assertEqual(-9, biggest(self.m17))
        self.assertEqual(self.m18, self.m17)
        
    def test_indices_biggest(self):
        self.assertEqual([0,0], indices_biggest(self.m1))
        self.assertEqual([0,0], indices_biggest(self.m2))
        self.assertEqual([0,0], indices_biggest(self.m3))
        self.assertEqual([2,2], indices_biggest(self.m5))
        self.assertEqual([1,1], indices_biggest(self.m8))
        self.assertEqual([2,1], indices_biggest(self.m13))
        self.assertEqual([0,2], indices_biggest(self.m16))
        self.assertEqual([1,2], indices_biggest(self.m14))
        self.assertEqual([2,2], indices_biggest(self.m17))
        self.assertEqual([1,2], indices_biggest(self.m25))
        
    def test_substr_in_values(self):
        d1 = {}
        d2 = {'dog':['rocket', 'patches', 'moca', 'latte']}
        d3 = {'dog':['rocket', 'patches', 'moca', 'latte'], 'cat':['crystal', 'shamrock']}
        d4 = {'DOG':['ROCKET'],'dog':['rocket']}
        self.assertEqual([], substr_in_values(d1, 'a'))
        self.assertEqual(['dog'], substr_in_values(d2, 'rock'))
        self.assertEqual([], substr_in_values(d2, 'sim'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, 'rock'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, 'ROCK'))
        self.assertEqual(['dog'], substr_in_values(d3, 'patch'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, ''))
        self.assertEqual(['DOG','dog'], substr_in_values(d4, 'ket'))
        
    def test_indices_divisible_by_3(self):
        self.assertEqual([], indices_divisible_by_3(self.m0))
        self.assertEqual([0], indices_divisible_by_3(self.m1))
        self.assertEqual([1], indices_divisible_by_3(self.m2))
        self.assertEqual([1], indices_divisible_by_3(self.m3))
        self.assertEqual([0], indices_divisible_by_3(self.m4))
        self.assertEqual([1, 6, 8], indices_divisible_by_3(self.m5))
        self.assertEqual([1, 6, 0], indices_divisible_by_3(self.m6))
        
    def test_sort_int_string(self):
        self.assertEqual("-17 4 42", sort_int_string("42 4 -17"))
        self.assertEqual("-3 -1", sort_int_string("-1 -3"))
        self.assertEqual("-17 4 42", sort_int_string("\t42   4 -17  \n"))
        self.assertEqual("3 3 3 4 4 4 5 5 5", sort_int_string("5 5 5 4 4 4 3 3 3"))
        self.assertEqual("", sort_int_string(""))
        self.assertEqual("", sort_int_string("\t"))
        self.assertEqual("1", sort_int_string("1"))
       
if __name__ == "__main__":
    test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFns)
    results = unittest.TextTestRunner().run(test)
    print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
