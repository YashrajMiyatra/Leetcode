import unittest
from solution import StreamChecker

class TestSolution(unittest.TestCase):
    def test_example1(self):
        checker = StreamChecker(["cd", "f", "kl"])
        self.assertFalse(checker.query("a"))
        self.assertFalse(checker.query("b"))
        self.assertFalse(checker.query("c"))
        self.assertTrue(checker.query("d"))
        self.assertFalse(checker.query("e"))
        self.assertTrue(checker.query("f"))
        self.assertFalse(checker.query("g"))
        self.assertFalse(checker.query("h"))
        self.assertFalse(checker.query("i"))
        self.assertFalse(checker.query("j"))
        self.assertFalse(checker.query("k"))
        self.assertTrue(checker.query("l"))
        
    def test_single_letter(self):
        checker = StreamChecker(["a"])
        self.assertTrue(checker.query("a"))
        self.assertTrue(checker.query("a"))
        self.assertFalse(checker.query("b"))

    def test_overlapping(self):
        checker = StreamChecker(["ab", "bab", "ba"])
        self.assertFalse(checker.query("b"))
        self.assertTrue(checker.query("a")) # suffix "ba"
        self.assertTrue(checker.query("b")) # suffix "ab", "bab"

if __name__ == '__main__':
    unittest.main()
