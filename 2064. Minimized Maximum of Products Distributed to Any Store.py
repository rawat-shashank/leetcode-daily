from typing import List
import unittest
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search on if it can be distributed among stoes equally
        def canDistribute(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n

        left, right = 1, max(quantities)
        res = 0
        while left <= right:
            x = (left + right) // 2
            if canDistribute(x):
                res = x
                right = x - 1
            else:
                left = x + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.minimizedMaximum(n=6, quantities=[11, 6]),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.minimizedMaximum(n=7, quantities=[15, 10, 10]),
        )

    def testcase3(self):
        self.assertEqual(
            100000,
            self.sol.minimizedMaximum(n=1, quantities=[100000]),
        )


if __name__ == "__main__":
    unittest.main()
