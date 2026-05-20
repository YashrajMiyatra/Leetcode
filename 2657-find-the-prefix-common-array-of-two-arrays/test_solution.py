import unittest
from solution import Solution

class TestFindThePrefixCommonArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        A = [1, 3, 2, 4]
        B = [3, 1, 2, 4]
        expected = [0, 2, 3, 4]
        self.assertEqual(self.solution.findThePrefixCommonArray(A, B), expected)

    def test_example_2(self):
        A = [2, 3, 1]
        B = [3, 1, 2]
        expected = [0, 1, 3]
        self.assertEqual(self.solution.findThePrefixCommonArray(A, B), expected)

    def test_single_element(self):
        # Minimum constraint: A.length == 1
        A = [1]
        B = [1]
        expected = [1]
        self.assertEqual(self.solution.findThePrefixCommonArray(A, B), expected)

    def test_identical_permutations(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.findThePrefixCommonArray(A, B), expected)

    def test_reversed_permutations(self):
        A = [1, 2, 3, 4, 5]
        B = [5, 4, 3, 2, 1]
        expected = [0, 0, 1, 3, 5]
        # Trace:
        # i=0: A=[1], B=[5] -> seen: {1:1, 5:1} -> 0 common
        # i=1: A=[1,2], B=[5,4] -> seen: {1:1, 2:1, 4:1, 5:1} -> 0 common
        # i=2: A=[1,2,3], B=[5,4,3] -> seen: {3:2} -> 1 common (3)
        # i=3: A=[1,2,3,4], B=[5,4,3,2] -> seen: {2:2, 3:2, 4:2} -> 3 common (2, 3, 4)
        # i=4: A=[1..5], B=[5..1] -> all common -> 5 common
        self.assertEqual(self.solution.findThePrefixCommonArray(A, B), expected)

if __name__ == '__main__':
    unittest.main()
