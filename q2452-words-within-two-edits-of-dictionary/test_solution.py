import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"]), ["word","note","wood"])

    def test_example_2(self):
        self.assertEqual(self.solution.twoEditWords(["yes"], ["not"]), [])

if __name__ == '__main__':
    unittest.main()
