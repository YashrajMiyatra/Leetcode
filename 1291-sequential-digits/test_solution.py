import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sequentialDigits(100, 300), [123,234])

    def test_example_2(self):
        self.assertEqual(self.solution.sequentialDigits(1000, 13000), [1234,2345,3456,4567,5678,6789,12345])

if __name__ == '__main__':
    unittest.main()
