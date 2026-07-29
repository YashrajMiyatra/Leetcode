import unittest
from solution import ProductOfNumbers

class TestProductOfNumbers(unittest.TestCase):
    def test_example_1(self):
        productOfNumbers = ProductOfNumbers()
        productOfNumbers.add(3)
        productOfNumbers.add(0)
        productOfNumbers.add(2)
        productOfNumbers.add(5)
        productOfNumbers.add(4)
        self.assertEqual(productOfNumbers.getProduct(2), 20)
        self.assertEqual(productOfNumbers.getProduct(3), 40)
        self.assertEqual(productOfNumbers.getProduct(4), 0)
        productOfNumbers.add(8)
        self.assertEqual(productOfNumbers.getProduct(2), 32)

if __name__ == '__main__':
    unittest.main()
