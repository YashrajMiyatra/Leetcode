import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15), [16, 33])

    def test_example_2(self):
        self.assertEqual(self.solution.beautifulIndices("abcd", "a", "a", 4), [0])

if __name__ == '__main__':
    unittest.main()
