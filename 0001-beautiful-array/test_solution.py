import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def is_beautiful(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    if 2 * arr[k] == arr[i] + arr[j]:
                        return False
        return True

    def test_example_1(self):
        res = self.solution.beautifulArray(4)
        self.assertEqual(len(res), 4)
        self.assertEqual(sorted(res), [1, 2, 3, 4])
        self.assertTrue(self.is_beautiful(res))

    def test_example_2(self):
        res = self.solution.beautifulArray(5)
        self.assertEqual(len(res), 5)
        self.assertEqual(sorted(res), [1, 2, 3, 4, 5])
        self.assertTrue(self.is_beautiful(res))

if __name__ == '__main__':
    unittest.main()
