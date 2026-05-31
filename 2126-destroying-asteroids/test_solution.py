import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertTrue(s.asteroidsDestroyed(10, [3,9,19,5,21]))

    def test_example_2(self):
        s = Solution()
        self.assertFalse(s.asteroidsDestroyed(5, [4,9,23,4]))

if __name__ == '__main__':
    unittest.main()
