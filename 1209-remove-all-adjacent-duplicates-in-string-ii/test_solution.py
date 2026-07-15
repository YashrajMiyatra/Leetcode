import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.removeDuplicates("abcd", 2), "abcd")

    def test_example_2(self):
        self.assertEqual(self.solution.removeDuplicates("deeedbbcccbdaa", 3), "aa")

    def test_example_3(self):
        self.assertEqual(self.solution.removeDuplicates("pbbcggttciiippooaais", 2), "ps")

if __name__ == '__main__':
    unittest.main()
