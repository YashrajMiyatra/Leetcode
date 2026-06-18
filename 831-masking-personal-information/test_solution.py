import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maskPII("LeetCode@LeetCode.com"), "l*****e@leetcode.com")

    def test_example_2(self):
        self.assertEqual(self.solution.maskPII("AB@qq.com"), "a*****b@qq.com")

    def test_example_3(self):
        self.assertEqual(self.solution.maskPII("1(234)567-890"), "***-***-7890")

    def test_phone_country_code(self):
        self.assertEqual(self.solution.maskPII("+86(888)888-8888"), "+**-***-***-8888")

if __name__ == '__main__':
    unittest.main()
