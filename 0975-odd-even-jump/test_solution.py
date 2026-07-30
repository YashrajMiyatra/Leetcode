import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.oddEvenJumps([10,13,12,14,15]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.oddEvenJumps([2,3,1,1,4]), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.oddEvenJumps([5,1,3,4,2]), 3)

if __name__ == '__main__':
    unittest.main()
