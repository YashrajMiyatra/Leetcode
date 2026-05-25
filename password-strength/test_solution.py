import unittest
from solution import Solution

class TestPasswordStrength(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        password = "aA1!"
        self.assertEqual(self.solution.passwordStrength(password), 11)

    def test_example_2(self):
        password = "bbB11#"
        self.assertEqual(self.solution.passwordStrength(password), 11)

    def test_only_lowercase(self):
        password = "abc"
        self.assertEqual(self.solution.passwordStrength(password), 3)

    def test_only_uppercase(self):
        password = "ABC"
        self.assertEqual(self.solution.passwordStrength(password), 6)

    def test_only_digits(self):
        password = "12345"
        self.assertEqual(self.solution.passwordStrength(password), 15)

    def test_only_specials(self):
        password = "!@#$"
        self.assertEqual(self.solution.passwordStrength(password), 20)

    def test_repeating_characters(self):
        password = "aaaaAAAA1111!!!!"
        # Unique: 'a' (+1), 'A' (+2), '1' (+3), '!' (+5)
        self.assertEqual(self.solution.passwordStrength(password), 11)

if __name__ == '__main__':
    unittest.main()
