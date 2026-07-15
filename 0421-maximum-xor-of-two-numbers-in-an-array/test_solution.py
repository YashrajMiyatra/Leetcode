import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMaximumXOR([3,10,5,25,2,8]), 28)

    def test_example_2(self):
        self.assertEqual(self.solution.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]), 127)

if __name__ == '__main__':
    unittest.main()
