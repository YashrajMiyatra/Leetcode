import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximizeActiveSection("01"), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maximizeActiveSection("0100"), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.maximizeActiveSection("1000100"), 7)

    def test_example_4(self):
        self.assertEqual(self.solution.maximizeActiveSection("01010"), 4)

if __name__ == '__main__':
    unittest.main()
