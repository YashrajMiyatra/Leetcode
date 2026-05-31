import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        items = [[6,2],[2,6],[3,4]]
        budget = 9
        self.assertEqual(s.maxItems(items, budget), 4)

    def test_example_2(self):
        s = Solution()
        items = [[2,4],[3,2],[4,1],[6,4],[12,4]]
        budget = 8
        self.assertEqual(s.maxItems(items, budget), 10)
        
    def test_identical_items(self):
        s = Solution()
        items = [[2,2], [2,2], [2,2]]
        budget = 6
        # Each gives 2 free copies. Total purchased = 3. Total free = 6.
        # Max items = 9
        self.assertEqual(s.maxItems(items, budget), 9)

if __name__ == '__main__':
    unittest.main()
