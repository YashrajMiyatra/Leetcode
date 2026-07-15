import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestConsecutive([100,4,200,1,3,2]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)

    def test_example_3(self):
        self.assertEqual(self.solution.longestConsecutive([1,0,1,2]), 3)

if __name__ == '__main__':
    unittest.main()
