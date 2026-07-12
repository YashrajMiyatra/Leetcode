import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.checkStrings("abcdba", "cabdab"), True)

    def test_example_2(self):
        self.assertEqual(self.solution.checkStrings("abe", "bea"), False)

if __name__ == '__main__':
    unittest.main()
