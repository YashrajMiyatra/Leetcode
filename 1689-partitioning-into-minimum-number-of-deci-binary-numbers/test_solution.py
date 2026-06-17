import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minPartitions("32"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minPartitions("82734"), 8)

    def test_example_3(self):
        self.assertEqual(self.solution.minPartitions("27346209830709182346"), 9)

if __name__ == '__main__':
    unittest.main()
