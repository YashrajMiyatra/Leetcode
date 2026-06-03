import unittest
from solution import Bank

class TestSolution(unittest.TestCase):
    def test_example(self):
        bank = Bank([10, 100, 20, 50, 30])
        self.assertTrue(bank.withdraw(3, 10))
        self.assertTrue(bank.transfer(5, 1, 20))
        self.assertTrue(bank.deposit(5, 20))
        self.assertFalse(bank.transfer(3, 4, 15))
        self.assertFalse(bank.withdraw(10, 50))

if __name__ == '__main__':
    unittest.main()
