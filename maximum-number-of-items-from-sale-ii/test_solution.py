import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        items = [[1,6],[2,4],[3,5]]
        budget = 19
        self.assertEqual(s.maximumSaleItems(items, budget), 5)

    def test_example_2(self):
        s = Solution()
        items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]]
        budget = 35
        self.assertEqual(s.maximumSaleItems(items, budget), 7)
        
    def test_identical_items(self):
        s = Solution()
        items = [[2,2], [2,2], [2,2]]
        budget = 6
        # Each gives 2 free copies limit.
        # Buying 3 total copies (one of each, or two of one and one of another) 
        # gives 3 free copies. Total = 6.
        self.assertEqual(s.maximumSaleItems(items, budget), 6)

if __name__ == '__main__':
    unittest.main()
