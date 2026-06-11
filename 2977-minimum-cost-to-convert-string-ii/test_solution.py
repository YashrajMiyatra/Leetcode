import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        source = "abcd"
        target = "acbe"
        original = ["a","b","c","c","e","d"]
        changed = ["b","c","b","e","b","e"]
        cost = [2,5,5,1,2,20]
        self.assertEqual(self.solution.minimumCost(source, target, original, changed, cost), 28)

    def test_example_2(self):
        source = "abcdefgh"
        target = "acdeeghh"
        original = ["bcd","fgh","thh"]
        changed = ["cde","thh","ghh"]
        cost = [1,3,5]
        self.assertEqual(self.solution.minimumCost(source, target, original, changed, cost), 9)

    def test_example_3(self):
        source = "abcdefgh"
        target = "addddddd"
        original = ["bcd","defgh"]
        changed = ["ddd","ddddd"]
        cost = [100,1578]
        self.assertEqual(self.solution.minimumCost(source, target, original, changed, cost), -1)

if __name__ == '__main__':
    unittest.main()
