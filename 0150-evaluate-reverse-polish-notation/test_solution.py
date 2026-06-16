import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.evalRPN(["2","1","+","3","*"]), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.evalRPN(["4","13","5","/","+"]), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

if __name__ == '__main__':
    unittest.main()
