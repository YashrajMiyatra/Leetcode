import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.decodeCiphertext("ch   ie   pr", 3), "cipher")

    def test_example_2(self):
        self.assertEqual(self.solution.decodeCiphertext("iveo    eed   l te   olc", 4), "i love leetcode")

    def test_example_3(self):
        self.assertEqual(self.solution.decodeCiphertext("coding", 1), "coding")

    def test_empty(self):
        self.assertEqual(self.solution.decodeCiphertext("", 1), "")

if __name__ == '__main__':
    unittest.main()
