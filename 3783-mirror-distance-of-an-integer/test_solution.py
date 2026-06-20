import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.mirrorDistance(25), 27)

    def test_example_2(self):
        self.assertEqual(self.solution.mirrorDistance(10), 9)

    def test_example_3(self):
        self.assertEqual(self.solution.mirrorDistance(7), 0)

if __name__ == '__main__':
    unittest.main()
