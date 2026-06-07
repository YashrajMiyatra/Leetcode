import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8])

    def test_example_2(self):
        self.assertEqual(self.solution.partitionLabels("eccbbbbdec"), [10])

if __name__ == '__main__':
    unittest.main()
