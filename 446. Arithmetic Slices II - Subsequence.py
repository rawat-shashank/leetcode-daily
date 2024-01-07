# 446. Arithmetic Slices II - Subsequence
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(7, self.sol.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))

    def testcase2(self):
        self.assertEqual(16, self.sol.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))


if __name__ == "__main__":
    unittest.main()
