import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.bulbSwitch(3), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.bulbSwitch(0), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.bulbSwitch(1), 1)

if __name__ == '__main__':
    unittest.main()
