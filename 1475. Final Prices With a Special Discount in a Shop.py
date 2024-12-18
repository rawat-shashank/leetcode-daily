import unittest
from typing import List


class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     """brute force, low constraints"""
    #     ans = []
    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             if prices[i] >= prices[j]:
    #                 ans.append(prices[i] - prices[j])
    #                 break
    #         if len(ans) < i + 1:
    #             ans.append(prices[i])
    #     return ans

    def finalPrices(self, prices: List[int]) -> List[int]:
        """O(n) - Monotonic stack"""
        stack = []
        res = prices[:]
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual([4, 2, 4, 2, 3], self.sol.finalPrices(prices=[8, 4, 6, 2, 3]))

    def testcase2(self):
        self.assertEqual([1, 2, 3, 4, 5], self.sol.finalPrices(prices=[1, 2, 3, 4, 5]))

    def testcase3(self):
        self.assertEqual(
            [9, 0, 1, 6],
            self.sol.finalPrices(prices=[10, 1, 1, 6]),
        )


if __name__ == "__main__":
    unittest.main()
