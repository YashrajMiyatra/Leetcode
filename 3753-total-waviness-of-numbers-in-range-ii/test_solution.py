import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.totalWaviness(120, 130), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.totalWaviness(198, 202), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.totalWaviness(4848, 4848), 2)

if __name__ == '__main__':
    unittest.main()
