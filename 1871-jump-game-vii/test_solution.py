import unittest
from solution import Solution

class TestJumpGameVII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "011010"
        minJump = 2
        maxJump = 3
        self.assertTrue(self.solution.canReach(s, minJump, maxJump))

    def test_example_2(self):
        s = "01101110"
        minJump = 2
        maxJump = 3
        self.assertFalse(self.solution.canReach(s, minJump, maxJump))

    def test_minimum_length_valid(self):
        s = "00"
        minJump = 1
        maxJump = 1
        self.assertTrue(self.solution.canReach(s, minJump, maxJump))

    def test_minimum_length_invalid(self):
        s = "01"
        minJump = 1
        maxJump = 1
        self.assertFalse(self.solution.canReach(s, minJump, maxJump))

    def test_large_jumps(self):
        s = "0110"
        minJump = 3
        maxJump = 3
        self.assertTrue(self.solution.canReach(s, minJump, maxJump))

    def test_alternating_invalid(self):
        s = "010101"
        minJump = 2
        maxJump = 2
        # Starts 0 -> can jump to 2.
        # From 2 -> s[2] is '0'. Can jump to 4.
        # From 4 -> s[4] is '0'. Can jump to 6 (out of bounds). Target is 5 (which is '1').
        self.assertFalse(self.solution.canReach(s, minJump, maxJump))

if __name__ == '__main__':
    unittest.main()
