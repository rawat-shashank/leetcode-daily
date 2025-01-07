import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0
        while right < len(prices):
            print(left, right)
            if prices[left] > prices[right]:
                left += 1
                right = left + 1
            else:
                profit = prices[right] - prices[left]
                res = max(res, profit)
                right += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]),
        )

    def testcase2(self):
        self.assertEqual(0, self.sol.maxProfit(prices=[7, 6, 4, 3, 1]))

    def testcase3(self):
        self.assertEqual(1, self.sol.maxProfit(prices=[1, 2]))

    def testcase4(self):
        self.assertEqual(2, self.sol.maxProfit(prices=[2, 1, 2, 1, 0, 1, 2]))


if __name__ == "__main__":
    unittest.main()
