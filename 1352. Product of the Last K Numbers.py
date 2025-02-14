import unittest
from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
            self.size = 0
        else:
            self.product.append(num * self.product[self.size])
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.product[self.size] // self.product[self.size - k]


class Testcases(unittest.TestCase):

    def testcase1(self):
        product_of_numbers = ProductOfNumbers()
        product_of_numbers.add(3)
        product_of_numbers.add(0)
        product_of_numbers.add(2)
        product_of_numbers.add(5)
        product_of_numbers.add(4)
        self.assertEqual(product_of_numbers.getProduct(2), 20)
        self.assertEqual(product_of_numbers.getProduct(3), 40)
        self.assertEqual(product_of_numbers.getProduct(4), 0)
        product_of_numbers.add(8)
        self.assertEqual(product_of_numbers.getProduct(2), 32)


if __name__ == "__main__":
    unittest.main()
