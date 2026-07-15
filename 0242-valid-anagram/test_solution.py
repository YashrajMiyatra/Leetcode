import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_example_2(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

if __name__ == '__main__':
    unittest.main()
