import unittest
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        l, r = 1, total // k
        res = 0
        while l <= r:
            m = (r + l) // 2
            count = 0
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.maximumCandies(candies = [5,8,6], k = 3),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.maximumCandies(candies = [2,5], k = 11),
        )


if __name__ == "__main__":
    unittest.main()
